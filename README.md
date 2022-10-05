# DIGITAL-IMAGING-INTERPRETATION
 A large variety of birds make the migration journey, and bird migration is one of the astonishments of the natural world. In this respect, you are given an image acquired during the bird migration in the South Pole of the Earth (birdmigration.jpg).
 
### 1. Split the given RGB image into 3 different grayscale images, and save the outputs in “tif” format.

RGB images can be split into 3 different grayscale images. 3 different grayscale images form the color image:

• Blue Channel(0),

• Green Channel(1),

• Red Channel(2).

Firstly, cv2 library is imported and “bird-migration.jpg”, blue image, green image and red image are defined.

![image](https://user-images.githubusercontent.com/54437726/194068746-d4caa8b9-3dfa-4f7a-97aa-40a323dfcd15.png)

For Blue Channel:

![image](https://user-images.githubusercontent.com/54437726/194069066-f62857d2-5349-43cd-9a7a-3965ae7b10f9.png)

For Green Channel:

![image](https://user-images.githubusercontent.com/54437726/194069121-6746fc72-f308-41ef-a3aa-a31f7e4493d3.png)

For Red Channel:

![image](https://user-images.githubusercontent.com/54437726/194069158-d10ea548-8206-466a-a4ff-9aa6c167d30f.png)

The outputs are:

![image](https://user-images.githubusercontent.com/54437726/194069277-03908243-f181-4a41-9a4c-5e0453d5452e.png)
Blue Channel

![image](https://user-images.githubusercontent.com/54437726/194069530-b537ccb8-d74b-4050-b289-29d129bed190.png)
Green Channel

![image](https://user-images.githubusercontent.com/54437726/194069586-32f23bd0-e512-45fd-9bcd-861d75a0fba8.png)
Red Channel

### 2. Create histogram of each grayscale image created in (1).

The id numbers of the blue, green and red channels are kept in a list “channel”. And the “cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])” function is used inside the for loop. This way, it gives the histogram of the grayscale images respectively.

![image](https://user-images.githubusercontent.com/54437726/194069903-4dc49441-dbb6-464b-8a48-e76f286d36a1.png)


The outputs are:

![image](https://user-images.githubusercontent.com/54437726/194070009-89916ef3-98dc-45be-a9c9-f46ac260fce3.png)
Blue Channel Histogram

![image](https://user-images.githubusercontent.com/54437726/194070081-1c3d1433-b6b8-4fc6-9e4c-ace128a48133.png)
Green Channel Histaogram

![image](https://user-images.githubusercontent.com/54437726/194070123-df1f5730-5aa5-4fde-8c03-a7b01f45d669.png)
Red Channel Histogram

### 3. Create image negatives of each grayscale image created in (1) without a python library.

• Inverting a digital image is a point processing operation.

• The output of image inversion is a negative of a digital image. 

• In a digital image the intensity levels vary from 0 to L-1. 

• The negative transformation is given by s=L-1-r. 

• When an image is inverted, each of its pixel value ‘r’ is subtracted from the maximum pixel value L-1 and the original pixel is replaced with the result ‘s’. 

• Image inversion or Image negation helps finding the details from the darker regions of the image. 

• The negative transformation has its applications in the areas of Medical Imaging, Remote Sensing and others.

![image](https://user-images.githubusercontent.com/54437726/194070470-274bd39d-e96d-4e91-b389-6539c43c6ae8.png)


The outputs are:

![image](https://user-images.githubusercontent.com/54437726/194070585-a1d9ba66-e2f1-4a1c-8d35-47a3ed773e14.png)
negative_b

![image](https://user-images.githubusercontent.com/54437726/194070640-132b086c-5ed6-4ba4-a1d6-eaa54975a0e3.png)
negative_g

![image](https://user-images.githubusercontent.com/54437726/194070666-b86da577-3380-4b2a-be9a-7758f6358383.png)
negative_r

### 4. With the help of one the grayscale images created in (1) or in (3), design and develop an algorithm (using a python code) that automatically counts the number of birds migrating. (without a python library)

![image](https://user-images.githubusercontent.com/54437726/194071057-0cfb1e21-6f28-45f8-bdd3-dcae4dc5e51c.png)


In this process, the grayscale image created in (1) is used (blue_image.tif). Once the image is defined, all pixels are crawled sequentially using for loops. And pixels with a value below 65 are converted to white(255). So the birds are aimed to be white and the rest to be black. As a result, the image looks like this:

![image](https://user-images.githubusercontent.com/54437726/194071110-56c2c4fa-ad48-4ff5-b2e7-22925984f8b9.png)


After that, a variable named “fltr” is defined. This variable fills a three by three matrix with white (white filter). Then, keep going by threes with nested for loops. If mean of matrix/mean of filter heigher than or equal to 0.5, this is a bird. So the total number of birds in this image is 41:

![image](https://user-images.githubusercontent.com/54437726/194071216-2745d964-5937-4555-b01e-8e1b8c938fde.png)

