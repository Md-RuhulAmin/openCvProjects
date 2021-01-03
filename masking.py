import cv2 as cv
import numpy as np

img = cv.imread('Images/dogs.jpg')
cv.imshow('Dogs', img)

blank = np.zeros(img.shape[:2],dtype= 'uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

# it is possible to draw different shape by using different wired shape from bitwise
#Also one important thing is that the blank iamge should have the exact size of the 
#original image, otherwise it not works

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)