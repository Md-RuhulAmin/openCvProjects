"""
# If an error shows like.... error: (-215:Assertion failed)
# It basically means that the file or folder is looking for is not found.
# Also after the video ends OpneCV show same error to tell that after video
# is finished ther is no more frame to interect with
"""
from cv2 import cv2 as cv

#Reading Images
# img = cv.imread('./Images/Nur.jpeg')
# cv.imshow('Nur', img)

#Reading Videos
capture = cv.VideoCapture('./Videos/Ruhul-live.mp4')

#Video is reading by while loop
while True:
    isTrue, frame = capture.read() #This basically read the video frame by frame
    cv.imshow('Video', frame)

    #To avoid play the video indefinitely
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

#Now realsing the capture pointer
capture.release()
#This is basically going to destroy all the GUI windows
cv.destroyAllWindows()

cv.waitKey(0)



