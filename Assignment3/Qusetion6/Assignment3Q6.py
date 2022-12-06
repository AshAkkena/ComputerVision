import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np 



# Image 1 is original image with marker
# Image 2 is translated with marker
img= cv2.imread("image1.jpg", 0)
img2= cv2.imread("image2.jpg", 0)
plt.figure(figsize = (20,2))
plt.imshow(img,cmap='gray', vmin=0, vmax=255)
plt.show()
plt.figure(figsize = (20,2))
plt.imshow(img2,cmap='gray', vmin=0, vmax=255)
plt.show()

D=640 
T=30
b=546.1 # distance between left and right cameras
f=1203.54736624058 #focallength
z=(b*f)/(D-T) #distance of object
print('The Disparity based depth estimation is '+str(z)+'mm')
