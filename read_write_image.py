import cv2
img=cv2.imread('lena.jpg')

cv2.imshow('outputimage',img)

cv2.imwrite('lenaoutput.jpg',img)
cv2.imwrite('lenaoutput.png',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
