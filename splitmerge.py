import cv2 as cv
import numpy as np

def rescaleFrame ( frame, scale=0.75):
    # This method will works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# img = rescaleFrame(cv.imread('Images/bg.jpg'), scale=0.2)

img = cv.imread('Images/bg.jpg')
cv.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([blue,green,red])
cv.imshow('Merged Image', merged)

cv.waitKey(0)