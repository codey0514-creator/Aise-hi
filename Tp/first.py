# import cv2 as cv
# #reading images
# img = cv.imread("ID.jpeg")
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# _, binary_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
# cv.imshow("ID" , binary_img)
# cv.waitKey(0)
#reading vedios 
        # capture = cv.VideoCapture("Aise hi/WhatsApp Video 2025-08-17 at 01.20.00.mp4")
        # while True :
        #     isTrue , frame = capture.read()
        #     cv.imshow("Vedio" , frame)
        #     if cv.waitKey(20) & 0xFF == ord("d"):
        #         break
        # capture.release()
        # cv.destroyAllWindows()
# img = cv.imread("Aise hi/ID.jpeg")
# cv.imshow("ID" , img)
# def rescaleFrame(frame , scale = 0.005):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)
#     dimensions = (width , height)
#     return cv.resize(frame, dimensions , interpolation= cv.INTER_AREA)
import cv2 as cv
import numpy as np
import math

def rotate(point, rx, ry, rz):
    x, y, z = point

    # Rotate around X
    y, z = y*math.cos(rx) - z*math.sin(rx), y*math.sin(rx) + z*math.cos(rx)

    # Rotate around Y
    x, z = x*math.cos(ry) + z*math.sin(ry), -x*math.sin(ry) + z*math.cos(ry)

    # Rotate around Z
    x, y = x*math.cos(rz) - y*math.sin(rz), x*math.sin(rz) + y*math.cos(rz)

    return x, y, z

# 8 cube vertices
cube = [
    (-1,-1,-1), (-1,-1,1), (-1,1,-1), (-1,1,1),
    (1,-1,-1),  (1,-1,1),  (1,1,-1),  (1,1,1)
]

edges = [
    (0,1),(0,2),(0,4),
    (3,1),(3,2),(3,7),
    (5,1),(5,4),(5,7),
    (6,2),(6,4),(6,7)
]

rx = ry = rz = 0

while True:
    frame = np.zeros((600,600,3), dtype="uint8")
    pts = []

    for p in cube:
        x, y, z = rotate(p, rx, ry, rz)
        scale = 100
        xp = int(300 + x*scale)
        yp = int(300 + y*scale)
        pts.append((xp, yp))

    for a,b in edges:
        cv.line(frame, pts[a], pts[b], (0,255,0), 2)

    cv.imshow("Cube", frame)

    rx += 0.02
    ry += 0.015
    rz += 0.01

    if cv.waitKey(20) == 27:
        break

