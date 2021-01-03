import cv2 as cv

def rescaleFrame ( frame, scale=0.75):
    # This method will works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
        # Here frame.shape[1] is width of the image and
        # frame.shape[0] is height of the image
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('./Images/Nur.jpeg') )
cv.imshow('Nur', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Eadges cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#Dilating the images
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500, 500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)