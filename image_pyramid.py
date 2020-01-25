import cv2
img=cv2.imread("lena.jpg")

smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)

cv2.imshow("original",img)
cv2.imshow("smaller ",smaller)
cv2.imshow("larger",larger)

cv2.waitKey()
cv2.destroyAllWindows()