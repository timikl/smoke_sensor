import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

from dotenv import load_dotenv

load_dotenv()

img_color = cv2.imread(os.getenv("IMAGE_PATH"), cv2.IMREAD_COLOR)
cv2.imshow("Sensor type A Back", img_color)

cv2.waitKey(0)

cv2.destroyAllwindows() 