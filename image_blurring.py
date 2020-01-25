import cv2
import numpy as np
img=cv2.imread("lena.jpg")
cv2.imshow("original",img)
cv2.waitKey(0)

#creating a 3x3kernel
kernel_3x3=np.ones((6,6),np.float32)/36

#we use cv2 filter2D to convolve the kernel with an image
blurred=cv2.filter2D(img,-1,kernel_3x3)
cv2.imshow("3x3 kernel blurring",blurred)
cv2.waitKey()

#creating a 7x7 kernel
kernel_7x7=np.ones((7,7),np.float32)/49

#we use cv2 filter2D to convolve the kernel with an image
blurred2=cv2.filter2D(img,-1,kernel_7x7)
cv2.imshow("7x7 kernel blurring",blurred2)
cv2.waitKey()

cv2.destroyAllWindows()