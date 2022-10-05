import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('bird-migration.jpg')
channel = [0,1,2]          # 0, 1 and 2 are the id numbers of the blue, green and red channels
for i in channel:
    hist = cv2.calcHist([img],[i],None,[256],[0,256])   # Calculating histogram
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()