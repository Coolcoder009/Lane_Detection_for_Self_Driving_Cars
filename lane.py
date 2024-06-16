# Normal Visualization(1)
import cv2 
import numpy as np
image=cv2.imread(r'Test/test_image.jpg')
# cv2.imshow('Lane Image',image)
# cv2.waitKey(0) 


# Canny Edge Detection(2) 
# 1.Conversion to Grey_Scale 2.Gaussian_Blur 3.Thresholding 4.ROI & Mask
temp=np.copy(image)
grey=cv2.cvtColor(temp,cv2.COLOR_RGB2GRAY) # Grey_Scale
# cv2.imshow('Grey_Scale Image',grey)
# cv2.waitKey(0) 
blur=cv2.GaussianBlur(grey,(5,5),0) # Gaussian_Blur
# cv2.imshow('Noise Reduced Image',blur)
# cv2.waitKey(0)  
canny=cv2.Canny(blur,50,150) # Thresholding
# cv2.imshow('Thresholded Image',canny)
# cv2.waitKey(0) 
height=image.shape[0] # ROI & Mask
polygons=np.array([[(200,height),(1100,height),(550,250)]])
mask=np.zeros_like(canny)
cv2.fillPoly(mask,polygons,255)
masked=cv2.bitwise_and(canny,mask)
# cv2.imshow('ROI & Masked Image',masked)
# cv2.waitKey(0) 

# Hough Transform
lines=cv2.HoughLinesP(masked,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5) 
# cv2.imshow('ROI & Masked Image',lines)
# cv2.waitKey(0) 






