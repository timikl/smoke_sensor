import cv2
import numpy as np
import matplotlib.pyplot as plt

img_color = cv2.imread('type_B_back.jpg//home/fikus/Desktop/Smoke_sensor/Pictures',cv2.IMREAD_COLOR)
cv2.imshow("Sensor type A Back", img_color)

cv2.waitKey(0)

cv2.destroyAllwindows() 