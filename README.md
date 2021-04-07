# Face-Swapper

## Ever wondered how to swap face of two subjects using python !! And that too using Matrix Manupulation ..

### Let's Do it !! 

### Step 1 : 
Take  a background Image 

![](input/comp_background.jpg) 

### Step 2 :
Take a foreground Image 

![](input/comp_foreground.jpg) 


### Step 3 : 
Make mask of the foreground Image

![](input/comp_mask.jpg) 


### Step 4 :
Using matrix operations access the each pixel in the Mask , Select the index value of pixels with value == 255 , and using that index value copy the pixel in Foreground Image and paste them in Background Image  

![](output/composite.jpg) 
