import cv2

img=cv2.imread("lena.jpg")

cv2.imshow('output',img)
print(img.shape)
print("height of the image in pixel is:",img.shape[0])
print("width of the image in pixel is:",img.shape[1])
print("layers in the image is:",img.shape[2])

cv2.waitKey(0)
cv2.destroyAllWindows()