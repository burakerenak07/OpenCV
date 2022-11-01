import cv2 as cv
import numpy as np

blank=np.zeros((900,900,3),dtype="uint8")
cv.imshow("Blank",blank)

# 1. Paint the image a certain colour
blank[200:300, 300:400]=0,255,0
cv.imshow("Red",blank)

# 2. draw Rectangle

# cv.rectangle(blank, (10,10),(250,250),(0,255,0),thickness=cv.FILLED)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank)

#3. Draw A circle

cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,255,0),thickness=3)
cv.imshow("Circle",blank)
cv.waitKey()