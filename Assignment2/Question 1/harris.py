import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
image = cv2.imread(sys.path[0]+"/img2.png", 1)
grayImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
grayImg = np.float32(grayImg)
dest = cv2.cornerHarris(grayImg,8, 29, 0.05)
dest = cv2.dilate(dest, None)
image[dest > 0.01 * dest.max()]=[0, 0, 255]
cv2.imwrite("Harris_img2.png",image)
cv2.imshow('Image with corners', image)
plt.imshow(image)
plt.show()