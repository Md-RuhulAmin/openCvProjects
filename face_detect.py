import cv2 as cv

def rescaleFrame ( frame, scale=0.75):
    # This method will works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('./Images/mim.jpg'), scale=0.2 )

# img = cv.imread ('Images/mim.jpg')
cv.imshow('Mim', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Mim Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

#Changing the value of the mineNeighbers can made the haarcascade more or less noise recogniser
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255,0), thickness=2)

cv.imshow('Detected faces', img)


cv.waitKey(0)