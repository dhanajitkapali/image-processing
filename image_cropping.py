import cv2
img=cv2.imread("lena.jpg")

height,width=img.shape[:2]

#getting the starting pixel coordinates for cropping ractangle
start_row,start_col=int(height*.25),int(width*.25)

#getting the end pixel coordinates for cropping rectanlge
end_row,end_col=int(height*.75),int(width*.80)

cropped_image=img[start_row:end_row,start_col:end_col]

cv2.imshow("original",img)
cv2.waitKey()

cv2.imshow("cropped",cropped_image)
cv2.waitKey()
cv2.destroyAllWindows()