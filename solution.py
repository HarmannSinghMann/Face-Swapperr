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
