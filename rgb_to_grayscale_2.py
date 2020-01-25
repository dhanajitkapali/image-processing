import cv2
img=cv2.imread("lena.jpg",0)
cv2.imshow("gray scale image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
