import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def convert_to_gps_coordinates(xdata, ydata, image_width, image_height, gps_bounds):
    # gps_bounds: (min_lat, max_lat, min_lon, max_lon)
    min_lat, max_lat, min_lon, max_lon = gps_bounds
    gps_coordinates = []
    for x, y in zip(xdata, ydata):
        lat = min_lat + (max_lat - min_lat) * (1 - y / image_height)
        lon = min_lon + (max_lon - min_lon) * (x / image_width)
        gps_coordinates.append((lat, lon))
    return gps_coordinates


class DrawingApp:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.xdata = []
        self.ydata = []
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.cid2 = self.fig.canvas.mpl_connect('motion_notify_event', self.onmousemove)
        self.cid3 = self.fig.canvas.mpl_connect('button_release_event', self.onrelease)
        self.drawing = False
        self.image_width = 800  # 실제 그림 영역의 너비
        self.image_height = 600  # 실제 그림 영역의 높이
        self.gps_bounds = (37.5, 37.6, 126.9, 127.0)  # 원하는 GPS 경계 설정

    def onclick(self, event):
        if event.inaxes is not None:
            self.drawing = True
            self.xdata.append(event.xdata)
            self.ydata.append(event.ydata)

    def onmousemove(self, event):
        if self.drawing and event.xdata and event.ydata:
            self.xdata.append(event.xdata)
            self.ydata.append(event.ydata)
            self.ax.plot(self.xdata, self.ydata, color='blue')
            plt.draw()

    def onrelease(self, event):
        self.drawing = False
        gps_coordinates = self.convert_to_gps_coordinates()
        print("GPS Coordinates:", gps_coordinates)
        plt.show()

    def convert_to_gps_coordinates(self):
        return convert_to_gps_coordinates(self.xdata, self.ydata,
                                          self.image_width, self.image_height,
                                          self.gps_bounds)


# 실행
app = DrawingApp()
plt.show()
