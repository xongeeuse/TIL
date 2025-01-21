import math
import requests
import folium


# 일단 거리만큼 경로 나눠서 요청하고 지도에 표시하기 성공

API_KEY = "2DWqj8ePnX9BcqL1xpG5B5N3Gfz32SwM4epGdQ9r"


def generate_coordinates(start_lat, start_lon, total_distance_km, num_points):
    R = 6371
    coordinates = [(start_lat, start_lon)]
    for i in range(1, num_points):
        segment_distance = (total_distance_km / (num_points - 1)) * i
        bearing = math.radians(45)
        start_lat_rad = math.radians(start_lat)
        start_lon_rad = math.radians(start_lon)

        new_lat_rad = math.asin(
            math.sin(start_lat_rad) * math.cos(segment_distance / R) +
            math.cos(start_lat_rad) * math.sin(segment_distance / R) * math.cos(bearing)
        )
        new_lon_rad = start_lon_rad + math.atan2(
            math.sin(bearing) * math.sin(segment_distance / R) * math.cos(start_lat_rad),
            math.cos(segment_distance / R) - math.sin(start_lat_rad) * math.sin(new_lat_rad)
        )

        new_lat = math.degrees(new_lat_rad)
        new_lon = math.degrees(new_lon_rad)
        coordinates.append((new_lat, new_lon))
    return coordinates


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
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("API 호출 실패:", response.status_code, response.text)
        return None


def get_full_route(coordinates):
    full_route = []
    for i in range(0, len(coordinates), 5):
        chunk = coordinates[i:i + 6]
        if len(chunk) > 2:
            start = chunk[0]
            end = chunk[-1]
            waypoints = chunk[1:-1]
            route_segment = call_tmap_api(start, end, waypoints)
            if route_segment:
                for feature in route_segment["features"]:
                    if feature["geometry"]["type"] == "LineString":
                        full_route.extend(feature["geometry"]["coordinates"])
    return full_route


def visualize_route(route):
    start_point = route[0]
    m = folium.Map(location=[start_point[1], start_point[0]], zoom_start=13)
    folium.PolyLine(locations=[[coord[1], coord[0]] for coord in route], color="blue", weight=2.5).add_to(m)
    folium.Marker([route[0][1], route[0][0]], popup="출발지").add_to(m)
    folium.Marker([route[-1][1], route[-1][0]], popup="도착지").add_to(m)
    m.save("tmap_route.html")
    print("경로가 tmap_route.html 파일에 저장되었습니다.")


# 메인 실행 부분
start_lat, start_lon = 35.092712, 128.911574
total_distance_km = 5
num_points = 20

coordinates = generate_coordinates(start_lat, start_lon, total_distance_km, num_points)
full_route = get_full_route(coordinates)

if full_route:
    visualize_route(full_route)
else:
    print("경로 생성에 실패했습니다.")
