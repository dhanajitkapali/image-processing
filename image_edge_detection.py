import cv2
import numpy as np
img=cv2.imread("lena.jpg",0)
cv2.imshow("original",img)
cv2.waitKey()

#extract slop edges
sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=9)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=9)

cv2.imshow("sobel_x image",sobel_x)
cv2.waitKey()

cv2.imshow("sobel_y image",sobel_y)
cv2.waitKey()

sobel_or=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("sobel or image",sobel_or)
cv2.waitKey()

laplacian=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('Laplacian image',laplacian)
cv2.waitKey()

canny=cv2.Canny(img,20,170)
cv2.imshow('canny edge',canny)
cv2.waitKey()

cv2.destroyAllWindows()
