import cv2 as cv
from matplotlib.scale import scale_factory

img= cv.imread("Resources/Photos/group 2.jpg")
cv.imshow("Person",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y), (x+w,y+h),(0,255,0), thickness=2)

cv.imshow("Detected Faces", img)
print(f'Number of faces found = {len(faces_rect)}')
cv.waitKey(0)