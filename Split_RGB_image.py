import cv2

img = cv2.imread("bird-migration.jpg")
img_blue = img[:,:,0]      # Blue band of the rgb image
img_green = img[:,:,1]     # Green band of the rgb image
img_red = img[:,:,2]       # Red band of the rgb image

cv2.imshow("Blue image",img_blue)    # To show the image
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("blue_image.tif",img_blue)     # To save the image

cv2.imshow("Green image",img_green)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("green_image.tif",img_green)

cv2.imshow("Red image",img_red)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("red_image.tif",img_red)