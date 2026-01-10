import cv2 as cv 
import math
import numpy as np
blank = np.zeros((500,500,3), dtype="uint8")
for i in range(360):          
    frame = blank.copy()
    angle = math.radians(i)
    a = 200 + 100 * (math.cos(angle) - math.sin(angle))
    b = 200 + 100 * (math.sin(angle) + math.cos(angle))
    a1 = 100 * (math.cos(angle) + math.sin(angle))
    b1 = 200 + 100 * (-math.sin(angle) + math.cos(angle))
    cv.line(frame, (200,200), (int(a1), int(b1)), (0,255,0), 2)
    cv.line(frame, (200,200), (int(a), int(b)), (0,255,0), 2)
    cv.imshow("line", frame)
    if cv.waitKey(70) == 27:   # <-- 70 ms delay (≈ 14 FPS)
        break
