import os
import cv2 as cv
import numpy as np

people = ['Bill_Gates','Elon_Musk','Greta_Thunberg','J_K_Rowling','Tom_Cruise']

DIR = r'/home/andrei/Desktop/recognizer/people'

features = list()
labels = list()

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
	for person in people:
		path = os.path.join(DIR,person)
		label = people.index(person)

		for img in os.listdir(path):
			img_path = os.path.join(path, img)

			img_array = cv.imread(img_path)
			gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
			faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 4)

			for (x,y,w,h) in faces_rect:
				face_region = gray[y:y+h,x:x+w]
				features.append(face_region)
				labels.append(label)
create_train()

face_recognizer = cv.face.LBPHFaceRecognizer_create()
features = np.array(features, dtype = 'object')
labels = np.array(labels)
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)