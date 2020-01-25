import cv2
import numpy as np
img=cv2.imread("lena.jpg")

height,width=img.shape[:2]
print(height)
print(width)

quarter_height,quarter_width=height/4,width/4
print(quarter_height)
print(quarter_width)

T=np.float32([[1,0,quarter_width],[0,1,quarter_height]])  #tarnslation matrix
print(T)

img_translation=cv2.warpAffine(img,T,(width,height))
cv2.imshow('original image',img)
cv2.imshow('translation',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()