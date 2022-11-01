import cv2 as cv

#reading photos
# img=cv.imread('Resources/Photos/cat_large.jpg')

def rescaleFrame(frame,scale=0.75):
    #images, videos and live video
    width= int(frame.shape[1] * scale)
    height=int(frame.shape[1] * scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions, interpolation= cv.INTER_AREA)

def changeRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)



#reading video

capture = cv.VideoCapture("C:/Users/burak/Desktop/Python03072022/OpenCV/Resources/Videos/dog.mp4")

while True:
    isTrue,frame=capture.read()

    frame_resized= rescaleFrame(frame,scale=.2)

    cv.imshow('Video',frame)
    cv.imshow('viedo Resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()