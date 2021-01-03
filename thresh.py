import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Images/dogs.jpg')
cv.imshow('Dogs', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Thresholdong 
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, 
cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', adaptive_thresh)

cv.waitKey(0)