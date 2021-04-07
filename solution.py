# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:10:46 2021

@author: Harmann Singh Mann


"""

import cv2
import numpy as np
import math

def NormalizeData(data):
       return (data - np.min(data)) / (np.max(data) - np.min(data))


def brightness(image,factor):

    # Normalised the input image
    image_nor = NormalizeData(image)

    # Incresed the brigtness of the image by the factor
    image_b = image_nor*factor

    return image_b


def convolution(oldimage, kernel):
    image_h = oldimage.shape[0]
    image_w = oldimage.shape[1]


    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    # Creating a padded image from input image by adding a padding of zeros around the image according to image shape
    if(len(oldimage.shape) == 3):
        image_pad = np.pad(oldimage, pad_width=((kernel_h // 2, kernel_h // 2),(kernel_w // 2, kernel_w // 2),(0,0)), mode='constant', constant_values=0).astype(np.float32)
    elif(len(oldimage.shape) == 2):
        image_pad = np.pad(oldimage, pad_width=((kernel_h // 2, kernel_h // 2),(kernel_w // 2, kernel_w // 2)), mode='constant', constant_values=0).astype(np.float32)


    h = kernel_h // 2
    w = kernel_w // 2

    # Created an Empty array of shape of the padded image
    image_conv = np.zeros(image_pad.shape)

    # Convolution operation using the Padded image + kernel and saving the results in empty padded array 'image_conv'
    for i in range(h, image_pad.shape[0]-h):
        for j in range(w, image_pad.shape[1]-w):
            #sum = 0
            x = image_pad[i-h:i-h+kernel_h, j-w:j-w+kernel_w]
            x = x.flatten()*kernel.flatten()
            image_conv[i][j] = x.sum()
    h_end = -h
    w_end = -w

    if(h == 0):
        return image_conv[h:,w:w_end]
    if(w == 0):
        return image_conv[h:h_end,w:]
    return image_conv[h:h_end,w:w_end]



def Blur(image, sigma):

    # Gaussian Filter size is defined same as the give in the problem statement
    filter_size = math.ceil((3*sigma)*2+1)
    gaussian_filter = np.zeros((filter_size, filter_size), np.float32)
    m = filter_size//2
    n = filter_size//2

    #Creating Gaussian filter using sigma
    for x in range(-m, m+1):
        for y in range(-n, n+1):
            x1 = 2*np.pi*(sigma**2)
            x2 = np.exp(-(x**2 + y**2)/(2* sigma**2))
            gaussian_filter[x+m, y+n] = (1/x1)*x2

    # Created an empty array of size of the image
    im_filtered = np.zeros_like(image, dtype=np.float32)

    # Now using the convolution function , performed the blur operation by passing the (image , gaussian filter) as parameters
    # Saving the results from convolution in empty array im_filtered which is of same size of image.

    for c in range(3):
        im_filtered[:, :, c] = convolution(image[:, :, c], gaussian_filter)
    return (im_filtered.astype(np.uint8))



def contrast(image,factor):

    #Created an empty array of same size of image
    new_image = np.zeros(image.shape, image.dtype)

    #Applied the contrast operation by multiplying the factor to each pixel and storing that in the empty array 'new_image'
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y,x,c] = factor*image[y,x,c]

    return new_image

def composite(background,foreground,mask):

    #Created a copy of the background image for safe reasons
    background_c = background.copy()

    # Manipulated the pixel values of mask : set the values > 0 as 255 .
    # I did this to easily extract the pixel position in mask while iterating over the images.
    mask2 = np.where(mask>0 , 255,0)

    # Searching for position of pixel values 255 in mask then using that position to copy values from foreground to background .
    for y in range(foreground.shape[0]):
        for x in range(foreground.shape[1]):
            for c in range(foreground.shape[2]):
                if mask2[y,x,c] == 255:
                    background_c[y,x,c] = foreground[y,x,c]
    return background_c


def ReadImage(path):

    #Using opencv to read the image from the directory
    image = cv2.imread(path)

    #For faster image operations I have decided to reduce the image size to 50% if the size > (600,800)
    if image.shape[0]>600 and image.shape[1]>800:
        image = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)


    #Converting the image to grayscale as will be used by edge detection and sharpen functions
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image,img_gray




if __name__ == "__main__":

    #Image path
    path ='input/princeton_small.jpg'

    # Read Image from path
    image,img_gray = ReadImage(path)

    cv2.imshow("Original-image", image)
    

    #Composite
    back = cv2.imread('input/comp_background.jpg')
    fore =cv2.imread('input/comp_foreground.jpg')
    mask = cv2.imread('input/comp_mask.jpg')
    image_comp = composite(back,fore,mask)
    cv2.imshow("Composite-Image", image_comp)

    # Press any key to terminate the output windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
