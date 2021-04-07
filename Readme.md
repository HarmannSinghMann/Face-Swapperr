# Image Processing - Without OpenCv

Hey , I have been using OpenCv extensively for the past few months and I thought its time for my own implementation of the Image Processing Filters using python.

# Description of code :
## Nature : 
This code takes in an image as input and gives output of all the functions (image processing operations) defined by me . The core of all operations is the CONVOLUTION operation of the matrices . 
![](input/convolution.png) 


## This code contains the following functions :
- Normalize Data - This function Normalizes the data in the range [0,1]                                - Parameter : (Image)
- Brightness     - This Function changes the brighness of the image by the given factor                - Parameter : (Image,Brightness Factor)
- Convolution    - This Function changes the brighness of the image by the given factor                - Parameter : (Image , kernel to convolute)
- Blur           - This function performs the blurr operation on the image by the factor of sigma      - Parameter : (Image , Blur factor-Sigma)
- Contrast       - This operations changes the contrast of the image by the given factor               - Parameter : (Image , Contrast factor)
- ReadImage      - This function is used to read the image from the given path


## Input Images
![](input/princeton_small.jpg) 
<a href="url"><img src="https://github.com/HarmannSinghMann/Image-Process-ing/blob/main/input/c.jpg" align="left" height="134" width="200" ></a>


# Filters: 
## 1. Brightness 
### This Function changes the brighness of the image by the given factor .

![](output/bright/princeton_small_brightness_0.jpg)![](output/bright/princeton_small_brightness_0.5.jpg) ![](output/bright/princeton_small_brightness_2.0.jpg) 
<br>
- Image 1: Brightness Factor = 0 
- Image 2: Brightness Factor = 0.5 
- image 3: Brightness Factor = 2.0

## 2. Blurr
### This function performs the blurr operation on the image by the factor of sigma.

![](output/blur/blur_0.125.jpg) ![](output/blur/blur_2.jpg) ![](output/blur/blur_8.jpg)
<br>
- Image 1 : Blurr Factor = 0.125 
- Image 2 : Blurr Factor = 2
- Image 3 : Blurr Factor = 8


## 3. Edge Detection
### This function performs the edge detection on the image by using the edge kernel(refer Readme.txt )
![](output/edge_d/edgedetect.jpg)

## 4. Sharpen
### This function performs the edge detection on the image by using the edge kernel(refer Readme.txt)
![](output/sharpen/sharpen.jpg)

## 5. Contrast
- Image 1 : Contrast Factor = -0.5 
- Image 2 : Contrast Factor = 0.0
- Image 3 : Contrast Factor = 0.5
- Image 4 : Contrast Factor = 2.0
<div class='container'>
<a href="url"><img src="https://github.com/HarmannSinghMann/Image-Process-ing/blob/main/output/contrast/c_contrast_-0.5.jpg" align="left" height="134" width="200" ></a>
<a href="url"><img src="https://github.com/HarmannSinghMann/Image-Process-ing/blob/main/output/contrast/c_contrast_0.0.jpg" align="left" height="134" width="200" ></a>
<a href="url"><img src="https://github.com/HarmannSinghMann/Image-Process-ing/blob/main/output/contrast/c_contrast_0.5.jpg" align="left" height="134" width="200" ></a>
<a href="url"><img src="https://github.com/HarmannSinghMann/Image-Process-ing/blob/main/output/contrast/c_contrast_2.0.jpg" align="left" height="134" width="200" ></a>
</div>


"# Face-Swapper" 
