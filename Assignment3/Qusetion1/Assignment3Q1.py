import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve,convolve2d
from PIL import Image
import numpy as np 
from collections import deque

vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 0
while success:
    success,image = vidcap.read()
    if count%30==0 :
      gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      cv2.imwrite("frammed/frame%d.jpg" % count, gray_image)     
      print('Stored a frame in frame%d.jpg'%count, success)
    count += 1

patch= cv2.imread("frammed/cropped.jpg", 0)
plt.axis('off')
plt.imshow(patch,cmap='gray', vmin=0, vmax=255)
plt.show()

for i in range(0,240,30):
    gray = cv2.imread("frammed/frame%d.jpg"%i, 0)
    patch= cv2.imread("frammed/cropped.jpg", 0)

    ssd = cv2.matchTemplate(gray, patch, cv2.TM_SQDIFF_NORMED) 

    point = np.where(ssd == ssd.min())
    y = point[0][0]
    x = point[1][0]
    w = len(patch[0])
    h = len(patch)

    plt.figure(figsize = (20,2))
    cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 2, 1), 2)
    plt.axis('off')
    plt.imshow(gray,cmap='gray', vmin=0, vmax=255)
    plt.show()
