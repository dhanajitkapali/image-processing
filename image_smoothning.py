import cv2
import numpy as np
img=cv2.imread("2.jpg")
cv2.imshow("original",img)
cv2.waitKey()

#averaging blur
blur=cv2.blur(img,(3,3))
cv2.imshow('blur image',blur )
cv2.waitKey()

#gaussian blur
Gaussian=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian blur image',Gaussian)
cv2.waitKey()

#median blur
median=cv2.medianBlur(img,5)
cv2.imshow('Median blur',median)
cv2.waitKey()

#bilateral
bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('bilateral blur image',bilateral)
cv2.waitKey()

cv2.destroyAllWindows()