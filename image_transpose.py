import cv2
img=cv2.imread('lena.jpg')

transposed_image=cv2.transpose(img)
cv2.imshow("transposed image",transposed_image)
cv2.waitKey(0)
cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()