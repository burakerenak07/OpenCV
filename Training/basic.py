from audioop import cross
import cv2 as cv

img= cv.imread('Resources\Photos\cat.jpg')
cv.imshow("Cat",img)

# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)




#blur

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade

canny= cv.Canny(blur,125,175)
cv.imshow('Canny Images', canny)

#Dilating the images 

dilated= cv.dilate(canny,(3,3), iterations=3)
cv.imshow('dilated', dilated)

# Eroding

eroded= cv.erode(dilated, (7,7),iterations=3 )
cv.imshow('eroded', eroded)

#Resize

resize= cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', resize)

#creapping
cropped= img[50:200 , 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0) 