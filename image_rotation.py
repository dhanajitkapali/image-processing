import cv2
import numpy as np
img=cv2.imread("lena.jpg")

height,width=img.shape[:2]

rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),120,.7)

rotated_image=cv2.warpAffine(img,rotation_matrix,(width,height))

cv2.imshow('rotated image',rotated_image)
cv2.waitKey(0)
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

