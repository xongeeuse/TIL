import matplotlib.pyplot as plt
import requests
import folium
import math

API_KEY = "2DWqj8ePnX9BcqL1xpG5B5N3Gfz32SwM4epGdQ9r"


# TMAP API 호출 함수
def call_tmap_api(data):
    url = "https://apis.openapi.sk.com/tmap/routes/pedestrian"
    headers = {
        "Content-Type": "application/json",
        "appKey": API_KEY
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("API 호출 실패:", response.status_code, response.text)
        return None


# TMAP 요청 데이터 준비 함수
def prepare_tmap_request_data(start, end, waypoints):
    pass_list = "_".join([f"{lon},{lat}" for lat, lon in waypoints])
    return {
        "startX": start[1],
        "startY": start[0],
        "endX": end[1],
        "endY": end[0],
        "passList": pass_list,
        "reqCoordType": "WGS84GEO",
        "resCoordType": "WGS84GEO",
        "startName": "출발지",
        "endName": "도착지"
    }


# 여러 번에 걸쳐 경로 요청 및 연결
def get_full_route(start, waypoints):
    full_route = []
    for i in range(0, len(waypoints), 5):
        chunk = waypoints[i:i + 5]

        # 시작점과 끝점을 설정
        chunk_start = start if i == 0 else chunk[0]
        chunk_end = waypoints[-1] if i + 5 >= len(waypoints) else chunk[-1]

        # 중간 경유지를 제외한 데이터 준비
        intermediate_waypoints = chunk[1:-1] if len(chunk) > 2 else []
        tmap_request_data = prepare_tmap_request_data(chunk_start, chunk_end, intermediate_waypoints)

        # API 호출
        tmap_response = call_tmap_api(tmap_request_data)

        if tmap_response:
            for feature in tmap_response["features"]:
                if feature["geometry"]["type"] == "LineString":
                    full_route.extend(feature["geometry"]["coordinates"])
            print(f"경로 {i // 5 + 1} 처리 완료.")
        else:
            print(f"경로 {i // 5 + 1} 처리 실패.")
            break

    return full_route


# 그림 좌표를 GPS로 변환 및 스케일 조정 함수
def convert_drawing_to_gps(xdata, ydata, image_width, image_height, gps_bounds, total_distance_km):
    def calculate_total_distance(coords):
        total_distance = 0
        for i in range(1, len(coords)):
            lat1, lon1 = coords[i - 1]
            lat2, lon2 = coords[i]
            R = 6371  # Earth radius in km
            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(
                dlon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            total_distance += R * c
        return total_distance

    min_lat, max_lat, min_lon, max_lon = gps_bounds
    gps_coordinates = []
    for x, y in zip(xdata, ydata):
        lat = min_lat + (max_lat - min_lat) * (1 - y / image_height)
        lon = min_lon + (max_lon - min_lon) * (x / image_width)
        gps_coordinates.append((lat, lon))

    current_distance = calculate_total_distance(gps_coordinates)
    scale_factor = total_distance_km / current_distance

    scaled_coordinates = []
    for i in range(len(gps_coordinates)):
        if i == 0:
            scaled_coordinates.append(gps_coordinates[i])
        else:
            prev_lat, prev_lon = scaled_coordinates[-1]
            dlat = (gps_coordinates[i][0] - prev_lat) * scale_factor
            dlon = (gps_coordinates[i][1] - prev_lon) * scale_factor
            scaled_coordinates.append((prev_lat + dlat, prev_lon + dlon))

    return scaled_coordinates


# 경로를 지도에 시각화하는 함수
def visualize_route_on_map(full_route):
    start_point = full_route[0]
    m = folium.Map(location=[start_point[1], start_point[0]], zoom_start=15)

    folium.PolyLine(locations=[[c[1], c[0]] for c in full_route], color="blue", weight=2.5).add_to(m)

    folium.Marker([start_point[1], start_point[0]], popup="출발지").add_to(m)

    end_point = full_route[-1]
    folium.Marker([end_point[1], end_point[0]], popup="도착지").add_to(m)

    m.save("tmap_full_route.html")
    print("전체 경로가 tmap_full_route.html 파일에 저장되었습니다.")


# 사용자 그림 입력 처리 클래스
class DrawingApp:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.xdata = []
        self.ydata = []
        self.drawing = False

        # 이벤트 연결
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_move)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)

        # GPS 변환 설정
        self.image_width = 500
        self.image_height = 500
        self.gps_bounds = (37.5, 37.6, 126.9, 127.0)

        # 총 경로 길이 설정 (5km)
        self.total_distance_km = 5

    def on_click(self, event):
        if event.inaxes is not None:
            self.drawing = True
            self.xdata.append(event.xdata)
            self.ydata.append(event.ydata)

    def on_move(self, event):
        if self.drawing and event.xdata and event.ydata:
            self.xdata.append(event.xdata)
            self.ydata.append(event.ydata)
            self.ax.plot(self.xdata[-2:], self.ydata[-2:], color='blue')
            plt.draw()

    def on_release(self, event):
        if self.drawing:
            self.drawing = False
            print("Drawing complete!")

            gps_coordinates = convert_drawing_to_gps(
                self.xdata,
                self.ydata,
                self.image_width,
                self.image_height,
                self.gps_bounds,
                self.total_distance_km,
            )

            print("Converted GPS Coordinates:", gps_coordinates)

            full_route_coords = get_full_route(gps_coordinates[0], gps_coordinates[1:])

            if full_route_coords:
                visualize_route_on_map(full_route_coords)


# 실행
app = DrawingApp()
plt.show()
