import numpy as np
import cv2
Paths=["D:/GSU/CV/Assignment2_Harshith/Question 2/imageset1/1.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset1//2.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset1//3.jpg"]
Paths2=["D:/GSU/CV/Assignment2_Harshith/Question 2/imageset2/1.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset2/2.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset2/3.jpg"]

Paths3=["D:/GSU/CV/Assignment2_Harshith/Question 2/imageset3/1.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset3/2.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset3/3.jpg"]

Paths4=["D:/GSU/CV/Assignment2_Harshith/Question 2/imageset4/1.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset4/2.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset4/3.jpg"]

Paths5=["D:/GSU/CV/Assignment2_Harshith/Question 2/imageset5/1.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset5/2.jpg",
         "D:/GSU/CV/Assignment2_Harshith/Question 2/imageset5/3.jpg"]

All_paths = [Paths,Paths2,Paths3,Paths4,Paths5]
imgset = []
i=1
for x in All_paths:	
	images = []
	for path in x:
		image = cv2.imread(path)
		images.append(image)
	print(len(images))
	stitcher = cv2.Stitcher_create()
	(status, stitched) = stitcher.stitch(images)
	if status == 0:
		print("Image Stitching Successful")
		cv2.imshow("Stitched Image", stitched)
		cv2.imwrite("stichedSet" + str(i) +  ".png",stitched)
	else:
		print("[INFO] Failed Image Stitching ({})".format(status))
	i+=1