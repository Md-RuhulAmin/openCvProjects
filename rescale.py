from cv2 import cv2 as cv

# As it recommened to go with lower piexels scale 
def rescaleFrame ( frame, scale=0.75):
    # This method will works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
        # Here frame.shape[1] is width of the image and
        # frame.shape[0] is height of the image
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#Reading Images
img = cv.imread('./Images/Nur.jpeg')
cv.imshow('Nur', img)

resized_image = rescaleFrame(img ) # Also can scale as like video frames
cv.imshow('Image', resized_image)

#THis function is specificly for videos to change the resolution
def changeRes ( width, height ):
    # only works on live videos
    capture.set(3, width)
    capture.set(4, height)

#Reading Videos
capture = cv.VideoCapture('./Videos/Ruhul-live.mp4')

while True: #Video is reading by while loop
    isTrue, frame = capture.read() #This basically read the video frame by frame

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('video Resized', frame_resized)

    #To avoid play the video indefinitely
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

#Now realsing the capture pointer
capture.release()
#This is basically going to destroy all the GUI windows
cv.destroyAllWindows()
