import cv2
import numpy as np
img=cv2.imread("lena.jpg")
cv2.imshow("original",img)
cv2.waitKey()

M=np.ones(img.shape,dtype="uint8")*150

added=cv2.add(img,M)
cv2.imshow("Added",added)

subtracted=cv2.subtract(img,M)
cv2.imshow("Subtracted",subtracted)

multiplied=cv2.multiply(img,M)
cv2.imshow("Multiply",multiplied)

cv2.waitKey()
cv2.destroyAllWindows()
