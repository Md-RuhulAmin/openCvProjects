import cv2 as cv
import numpy as np

# To get a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('./Images/Nur.jpeg')
# cv.imshow('Nur', img)

# 1. Paint the image a cetain color
# blank[:] = 0,255,0 # For green color
# blank[:] = 0,0,255 # for red color
# blank[200:300, 300:400] = 0,0,255 # To get a certain part colored
# cv.imshow('Green', blank)

#2. Draw rectange
# cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=2)
# cv.imshow('Rectangle', blank)

# 3. draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('Circle', blank)


# 4. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3 )
# cv.imshow('Line', blank)

# 5. write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)