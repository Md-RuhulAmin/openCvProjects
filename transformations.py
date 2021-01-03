import cv2 as cv
import numpy as np

def rescaleFrame ( frame, scale=0.75):
    # This method will works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('./Images/Ruhul.jpg'), scale=0.2 )
cv.imshow('Ruhul', img)

# Translation
def translate (img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)


#Rotation
def rotate (img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)

    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

#Flipping
flip = cv.flip(img, 1) # 0 to flip vertically, 1 to flip horizontally, -1 flip vertically anf horizontally
cv.imshow('Flip', flip)

cv.waitKey(0)