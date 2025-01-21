import matplotlib.pyplot as plt
import pprint
import requests
import folium


API_KEY = "2DWqj8ePnX9BcqL1xpG5B5N3Gfz32SwM4epGdQ9r"

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


def visualize_tmap_route(route_data):
    coordinates = []
    for feature in route_data["features"]:
        if feature["geometry"]["type"] == "LineString":
            coordinates.extend(feature["geometry"]["coordinates"])

    lons, lats = zip(*coordinates)

    plt.figure(figsize=(10, 8))
    plt.plot(lons, lats, marker='o', color='red', label='TMAP Route')
    plt.title('TMAP Pedestrian Route')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid()
    plt.show()


def prepare_tmap_request_data(gps_coordinates):
    start_y, start_x = gps_coordinates[0]  # 위도, 경도 순서 변경
    end_y, end_x = gps_coordinates[-1]  # 위도, 경도 순서 변경
    pass_list = "_".join([f"{lon},{lat}" for lat, lon in gps_coordinates[1:-1]])

    return {
        "startX": start_x,
        "startY": start_y,
        "endX": end_x,
        "endY": end_y,
        "passList": pass_list,
        "reqCoordType": "WGS84GEO",
        "resCoordType": "WGS84GEO",
        "startName": "출발지",
        "endName": "도착지"
    }



# 1. 그림 좌표를 GPS 좌표로 변환하는 함수
def convert_drawing_to_gps(xdata, ydata, image_width, image_height, gps_bounds):
    min_lat, max_lat, min_lon, max_lon = gps_bounds
    gps_coordinates = []
    for x, y in zip(xdata, ydata):
        lat = min_lat + (max_lat - min_lat) * (1 - y / image_height)
        lon = min_lon + (max_lon - min_lon) * (x / image_width)
        gps_coordinates.append((lat, lon))
    return gps_coordinates

# 2. GPS 경로를 중심점에 맞게 조정하는 함수
def adjust_route_to_start(center_lat, center_lon, gps_coordinates):
    lat_offset = center_lat - gps_coordinates[0][0]
    lon_offset = center_lon - gps_coordinates[0][1]
    adjusted_route = [(lat + lat_offset, lon + lon_offset) for lat, lon in gps_coordinates]
    return adjusted_route

# 3. 경로를 시각화하는 함수
def visualize_route(route):
    lats, lons = zip(*route)
    plt.figure(figsize=(8, 6))
    plt.plot(lons, lats, marker='o', color='blue', label='Running Route')
    plt.title('Generated Running Route')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid(True)
    plt.show()

# 4. 사용자 그림 입력을 처리하는 클래스
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
            )
            current_lat = 37.5665
            current_lon = 126.9780
            running_route = adjust_route_to_start(current_lat, current_lon, gps_coordinates)

            print("Converted GPS Coordinates:", running_route)

            tmap_request_data = prepare_tmap_request_data(running_route)
            tmap_response = call_tmap_api(tmap_request_data)

            if tmap_response:
                pprint.pprint(tmap_response)
                visualize_tmap_route(tmap_response)

                # Folium 지도 생성
                start_point = tmap_response['features'][0]['geometry']['coordinates']
                start_lat, start_lon = start_point[1], start_point[0]
                m = folium.Map(location=[start_lat, start_lon], zoom_start=15)

                coordinates = []
                for feature in tmap_response['features']:
                    if feature['geometry']['type'] == 'LineString':
                        coords = feature['geometry']['coordinates']
                        coordinates.extend(coords)
                        folium.PolyLine(locations=[[c[1], c[0]] for c in coords], color="blue", weight=2.5,
                                        opacity=1).add_to(m)

                folium.Marker([start_lat, start_lon], popup="출발지").add_to(m)
                end_point = coordinates[-1]
                folium.Marker([end_point[1], end_point[0]], popup="도착지").add_to(m)

                m.save("tmap_route.html")
            else:
                print("TMAP API 호출 실패")

            visualize_route(running_route)


# 실행
app = DrawingApp()
plt.show()
#
# import folium
# import json
#
# # TMAP API 응답 데이터 (JSON 형식으로 가정)
# tmap_response = json.loads(response.text)
#
# # 시작점 좌표 추출
# start_point = tmap_response['features'][0]['geometry']['coordinates']
# start_lat, start_lon = start_point[1], start_point[0]
#
# # 지도 생성
# m = folium.Map(location=[start_lat, start_lon], zoom_start=15)
#
# # 경로 좌표 추출 및 지도에 표시
# coordinates = []
# for feature in tmap_response['features']:
#     if feature['geometry']['type'] == 'LineString':
#         coords = feature['geometry']['coordinates']
#         coordinates.extend(coords)
#         folium.PolyLine(locations=[[c[1], c[0]] for c in coords], color="blue", weight=2.5, opacity=1).add_to(m)
#
# # 시작점과 도착점 마커 추가
# folium.Marker([start_lat, start_lon], popup="출발지").add_to(m)
# end_point = coordinates[-1]
# folium.Marker([end_point[1], end_point[0]], popup="도착지").add_to(m)
#
# # 지도 저장
# m.save("tmap_route.html")
