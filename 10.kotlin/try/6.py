import math
import requests
import folium
import matplotlib.pyplot as plt



# GPS 좌표 변환 및 스케일링 함수
def convert_drawing_to_scaled_gps(xdata, ydata, image_width, image_height, gps_bounds, total_distance_km):
    def calculate_total_distance(coords):
        total_distance = 0
        for i in range(1, len(coords)):
            lat1, lon1 = coords[i - 1]
            lat2, lon2 = coords[i]
            R = 6371  # Earth radius in km
            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
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
    scale_factor = total_distance_km / current_distance if current_distance > 0 else 1

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

# TMAP API 호출 함수
def call_tmap_api(start, end, waypoints):
    url = "https://apis.openapi.sk.com/tmap/routes/pedestrian"
    headers = {
        "Content-Type": "application/json",
        "appKey": API_KEY
    }
    pass_list = "_".join([f"{lon},{lat}" for lat, lon in waypoints])
    data = {
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

    print("API 요청 데이터:", data)  # 요청 데이터 출력

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 204:
        print("API 호출 성공: 경로를 찾을 수 없습니다 (204 No Content).")
    else:
        print(f"API 호출 실패: {response.status_code}, {response.text}")

    return None


# Folium 지도 시각화 함수
def visualize_route(route_data):
    m = folium.Map(location=[route_data['features'][0]['geometry']['coordinates'][1],
                             route_data['features'][0]['geometry']['coordinates'][0]],
                   zoom_start=13)

    for feature in route_data['features']:
        if feature['geometry']['type'] == 'LineString':
            folium.PolyLine(locations=[[coord[1], coord[0]] for coord in feature['geometry']['coordinates']],
                            color="blue", weight=2.5).add_to(m)

    m.save("tmap_route.html")
    print("경로가 tmap_route.html 파일에 저장되었습니다.")

# 그림 입력 클래스
class DrawingApp:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.xdata = []
        self.ydata = []
        self.drawing = False

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_move)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)

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
            self.process_drawing()

    def process_drawing(self):
        scaled_coordinates = convert_drawing_to_scaled_gps(
            self.xdata, self.ydata,
            image_width=500,
            image_height=500,
            gps_bounds=(35.0, 36.0, 128.0, 129.0),
            total_distance_km=5
        )

        start = scaled_coordinates[0]
        end = scaled_coordinates[-1]
        waypoints = scaled_coordinates[1:-1]

        route_data = call_tmap_api(start, end, waypoints)

        if route_data:
            visualize_route(route_data)
        else:
            print("경로 생성에 실패했습니다.")

# 실행
if __name__ == "__main__":
    app = DrawingApp()
    plt.show()
