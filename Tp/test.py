import cv2 as cv
import numpy as np
import math
def rotate3D(point, rx, ry, rz):
    x, y, z = point
    y, z = y*math.cos(rx) - z*math.sin(rx), y*math.sin(rx) + z*math.cos(rx)
    x, z = x*math.cos(ry) + z*math.sin(ry), -x*math.sin(ry) + z*math.cos(ry)
    x, y = x*math.cos(rz) - y*math.sin(rz), x*math.sin(rz) + y*math.cos(rz)
    return x, y, z
P0 = (0, 0, 0)
P1 = (100, 0, 0)
cx, cy = 250, 250
rx = ry = rz = 0
while True:
    frame = np.zeros((500, 500, 3), dtype=np.uint8)
    x, y, z = rotate3D(P1, rx, ry, rz)
    screen_x0 = int(cx + P0[0])
    screen_y0 = int(cy - P0[1])
    screen_x1 = int(cx + x)
    screen_y1 = int(cy - y)
    cv.line(frame, (screen_x0, screen_y0), (screen_x1, screen_y1), (0, 255, 0), 2)
    cv.imshow("3D Line", frame)
    rx += 0.02
    ry += 0.015
    rz += 0.01
    if cv.waitKey(20) == 27:
        break
