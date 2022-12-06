import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
#This script generates homography matrix
src_points = np.array([[275,319],[796,313],[769,575],[251,535]])
dest_points = np.array([[651,446],[968,442],[996,591],[657,598]])
h, status = cv2.findHomography(src_points, dest_points)
print("Homography Matrix:" + str(h))
im_src = cv2.imread(sys.path[0]+'/img1.png',1)
im_dst = cv2.imread(sys.path[0]+'/img2.png')
#this will give warped image output using h as homography matrix
im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
cv2.imshow("Warped_Source_Image", im_out)
plt.imshow(im_out)
plt.show()