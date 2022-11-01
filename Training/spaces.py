import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Resources\Photos\group 1.jpg")
cv.imshow("Group-1",img)

# plt.imshow(img)
# plt.show()

# #BGR to GRAYSCALE

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# BGR HSV

hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

# BGR to L*a*b

lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

#BGR to RGB

rgb= cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

# HSV to BGR
hsv_bgr= cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_bgr)


plt.imshow(rgb)
plt.show()

cv.waitKey(0)