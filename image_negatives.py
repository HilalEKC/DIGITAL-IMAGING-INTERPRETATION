import cv2

img1 = cv2.imread('blue_image.tif')
img1_negative = 1 - img1                        # Negative image formula
cv2.imshow("blue_negative", img1_negative) 
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("negative_b.tif",img1_negative)     # Saving negative image for blue band of rgb image

img2 = cv2.imread('green_image.tif')
img2_negative = 1 - img2
cv2.imshow("green_negative", img2_negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("negative_g.tif",img2_negative)     # Saving negative image for green band of rgb image

img3 = cv2.imread('red_image.tif')
img3_negative = 1 - img3
cv2.imshow("red_negative", img3_negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("negative_r.tif",img3_negative)     # Saving negative image for red band of rgb image