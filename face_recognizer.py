import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
people = ['Bill_Gates','Elon_Musk','Greta_Thunberg','J_K_Rowling','Tom_Cruise']
haar_cascade_face = cv.CascadeClassifier('haar_face.xml')
haar_cascade_profile = cv.CascadeClassifier('haar_profile.xml')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
while True:
	isTrue, frame = capture.read() 
	
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	faces_rect = haar_cascade_face.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 4)
	profile_rect = haar_cascade_profile.detectMultiScale(gray,scaleFactor = 1.2, minNeighbors = 4)
	detections = []

	if (faces_rect != ()):
		detections.append(faces_rect[0])
	if (profile_rect != ()):
		detections.append(profile_rect[0])
		
	for (x,y,w,h) in detections:
		face_region = gray[y:y+h,x:x+w]
		label, confidence = face_recognizer.predict(face_region)
		cv.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),thickness=2)
		cv.rectangle(frame, (x,y-45), (x+w+2,y-2),(0,255,0),-1)
		cv.putText(frame,people[label].replace('_',' '),(x,y-10),cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255),2)
	cv.imshow('Frame',frame)
	if cv.waitKey(20) & 0xFF == ord('q'):
		break



capture.release()
cv.destroyAllWindows()