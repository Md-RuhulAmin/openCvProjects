import os
import cv2 as cv
import numpy as np


# p = []
# for i in os.listdir(r'E:\openCVProjects\Photos'):
#     p.append(i)
# print(p)

people = ['Lady Gaga', 'Leonardo Dicaprio', 'Madonna', 'Mim', 'Momshad', 'Ruhul']
DIR = r'E:\openCVProjects\Photos'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features =[]
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,
            minNeighbors=4)

            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print('Training done ---------------------')

# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

features =np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)