import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
captured_image = cv2.imread(sys.path[0]+"/img1.png", 1)
edge_image = cv2.Canny(captured_image,180,200)
cv2.imwrite("canny_edge_output.png",captured_image)
plt.imshow(captured_image)
plt.imshow(edge_image,cmap="gray")
plt.show()