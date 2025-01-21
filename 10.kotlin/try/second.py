import math
import matplotlib.pyplot as plt

# 1. 그림 좌표를 GPS 좌표로 변환
def convert_drawing_to_gps(xdata, ydata, image_width, image_height, gps_bounds):
    min_lat, max_lat, min_lon, max_lon = gps_bounds
    gps_coordinates = []
    for x, y in zip(xdata, ydata):
        lat = min_lat + (max_lat - min_lat) * (1 - y / image_height)
        lon = min_lon + (max_lon - min_lon) * (x / image_width)
        gps_coordinates.append((lat, lon))
    return gps_coordinates

# 2. GPS 경로를 중심점에 맞게 조정
def adjust_route_to_start(center_lat, center_lon, gps_coordinates):
    lat_offset = center_lat - gps_coordinates[0][0]
    lon_offset = center_lon - gps_coordinates[0][1]
    adjusted_route = [(lat + lat_offset, lon + lon_offset) for lat, lon in gps_coordinates]
    return adjusted_route

# 3. 경로를 시각화
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

            # GPS 변환 및 경로 시각화
            gps_coordinates = convert_drawing_to_gps(
                self.xdata,
                self.ydata,
                self.image_width,
                self.image_height,
                self.gps_bounds,
            )
            current_lat = 37.5665  # 서울의 위도 (출발점 예시)
            current_lon = 126.9780  # 서울의 경도 (출발점 예시)
            running_route = adjust_route_to_start(current_lat, current_lon, gps_coordinates)

            # 변환된 GPS 좌표 출력
            print("Converted GPS Coordinates:", running_route)

            visualize_route(running_route)

# 실행
app = DrawingApp()
plt.show()





#
#
#
# '''
# TMAP API 보행자 경로 요청
# '''
#
#
# import requests
#
# # TMAP API Key

#
# # 출발지, 도착지, 경유지 정보
# start_x = 126.9780  # 출발지 경도
# start_y = 37.5665   # 출발지 위도
# end_x = 126.9870    # 도착지 경도
# end_y = 37.5650     # 도착지 위도
# pass_list = "126.9820,37.5640_126.9840,37.5635"  # 경유지 (경도,위도 형식으로 '_'로 구분)
#
# # 요청 데이터
# url = "https://apis.openapi.sk.com/tmap/routes/pedestrian"
# headers = {
#     "Content-Type": "application/json",
#     "appKey": API_KEY
# }
# data = {
#     "startX": start_x,
#     "startY": start_y,
#     "endX": end_x,
#     "endY": end_y,
#     "passList": pass_list,
#     "reqCoordType": "WGS84GEO",
#     "resCoordType": "WGS84GEO",
#     "startName": "출발지",
#     "endName": "도착지"
# }
#
# # API 호출
# response = requests.post(url, headers=headers, json=data)
#
# # 결과 확인
# if response.status_code == 200:
#     result = response.json()
#     print("경로 탐색 결과:", result)
# else:
#     print("API 호출 실패:", response.status_code, response.text)
