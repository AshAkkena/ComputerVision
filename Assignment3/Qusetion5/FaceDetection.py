import cv2
import matplotlib as plt
face_detector_model = cv2.CascadeClassifier('face.xml')

# reading the input image now
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector_model.detectMultiScale(gray,1.1, 4 )
    for (x,y, w, h) in faces:
        cv2.putText(frame, "Person1", (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.rectangle(frame, pt1 = (x,y),pt2 = (x+w, y+h), color = (255,0,0),thickness =  3)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.imshow("window", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#Detect faces
patch= cv2.imread("face.png", 0)
plt.figure(figsize = (20,2))
plt.imshow(patch,cmap='gray', vmin=0, vmax=255)
plt.show()

# After testing with live faces and random objects
# TP : 7 FP: 10 TN: 3 FN: 0
# Accuracy  = (TruePositives + FalsePositives) / (TruePositives + FalsePositives + FalseNegatives + TrueNegatives)
# Accuracy = 17/20 = 0.85 (approx)
# Precision = TruePositives / (TruePositives + FalsePositives)
# Precision = 7 / 17 = 0.411 (approx)
# Recall = TruePositives / (TruePositives + FalseNegatives)
# Recall = 7 / 7 = 1