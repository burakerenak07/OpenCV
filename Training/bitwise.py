import cv2 as cv
from cv2 import circle
import numpy as np

blank= np.zeros((400,400), dtype="uint8")

rectangle= cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circles= cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circles)

#bitwise AND

bitwise_and= cv.bitwise_and(rectangle,circles)
cv.imshow("Bitwise AND", bitwise_and)



cv.waitKey(0)