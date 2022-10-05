import cv2
import numpy as np

img = cv2.imread("blue_image.tif",0)
                                                                   
for i in range(0,img.shape[0]):    #width
    for j in range(0,img.shape[1]):   #height
        if img[i,j] <= 65:     #if the pixel value is <=65, then convert it white
            img[i,j] = 255
        else:
            img[i,j] = 0   #if the pixel value is >65, then convert it black
fltr =  np.full((3,3),255)      # Fills a three by three matrix with white (white filter)
number_of_birds = 0
for i in range(0,img.shape[0],3):    #keep going the filter by threes
    for j in range(0,img.shape[1],3):
        if img[i:i+4,j:j+4].mean() / fltr.mean() >= 0.50:  # mean of matrix/mean of filter. Thus, a value is set. if it is>=50, this is a bird.
            number_of_birds += 1
print(number_of_birds)
cv2.imshow("birds",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




