
import cv2
def on_click(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, ' ', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +str(y), (x,y), font,1, (255, 0, 0), 2)
		cv2.imshow('image', img)
	if event==cv2.EVENT_RBUTTONDOWN:
		print(x, ' ', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('image', img)
img = cv2.imread('img2C.png')
img= cv2.resize(img, (1000,1000 ))
cv2.imwrite("CornersImage.png",img)

cv2.imshow('image', img)

cv2.setMouseCallback('image', on_click)
cv2.waitKey(0)
cv2.destroyAllWindows()
