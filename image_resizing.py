import cv2
img=cv2.imread("lena.jpg")
cv2.imshow("original image",img)
cv2.waitKey()

img_scaled=cv2.resize(img,None,fx=0.75,fy=0.75)              #resize to 3/4 size
cv2.imshow('Saling-Linear Interpolation',img_scaled)
cv2.waitKey()

img_scaled1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)#double the size
cv2.imshow('scalig-cubic interpolation',img_scaled1)
cv2.waitKey()

img_scaled2=cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow('scalig-skewed size',img_scaled2)
cv2.waitKey()

cv2.destroyAllWindows()



