from turtle import width
import cv2 as cv 
import numpy as np

img= cv.imread("Resources\Photos\group 1.jpg")

cv.imshow("Group-1",img)

#Translation

def translate(img,x,y):

    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated=translate(img, -100,100)
cv.imshow("translated",translated)


#Rotation

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint= (width//2,height//2)
        rotMat=cv.getRotationMatrix2D(rotPoint,angle,.0)
        dimensions=(width,height)

        return cv.warpAffine(img, rotMat,dimensions)
    


rotated=rotate(img,-45)
cv.imshow('Rotated', rotated)

rotated_rotated=rotate(rotated,-45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized= cv.resize(img,(1920,1080), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping

flip=cv.flip(img,0)
cv.imshow("flip",flip)

# Cropping
cropped=img[200:400,300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)