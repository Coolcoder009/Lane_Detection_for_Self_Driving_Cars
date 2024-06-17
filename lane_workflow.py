# Normal Visualization(1)
import cv2 
import numpy as np
image=cv2.imread(r'Test/test_image.jpg')
# cv2.imshow('Lane Image',image)
# cv2.waitKey(0) 
def coordinates(image,param):
    slope,intercept=param
    y1=image.shape[0]
    y2=int(y1*(3/5))
    x1=int((y1-intercept)/slope)
    x2=int((y2-intercept)/slope)
    return np.array([x1,y1,x2,y2])

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
line_image=np.zeros_like(temp)
if lines is not None:
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
# cv2.imshow('line',line_image)
# cv2.waitKey(0)
combo_image=cv2.addWeighted(temp,0.7,line_image,2,2)
# cv2.imshow('line',combo_image)
# cv2.waitKey(0) 
left_fit=[]
right_fit=[]
for line in lines:
    x1,y1,x2,y2=line.reshape(4)
    param=np.polyfit((x1,x2),(y1,y2),1)
    slope=param[0]
    intercept=param[1]
    if slope<0:
        left_fit.append((slope,intercept))
    else:
        right_fit.append((slope,intercept))
left_fit_avg=np.average(left_fit,axis=0)
right_fit_avg=np.average(right_fit,axis=0) 
left_line=coordinates(temp,left_fit_avg)
right_line=coordinates(temp,right_fit_avg)
arr=np.array([left_line,right_line])
line_image=np.zeros_like(temp)
if arr is not None:
    for line in arr:
        x1,y1,x2,y2=line.reshape(4)
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
comb_image=cv2.addWeighted(temp,0.7,line_image,2,2)
cv2.imshow('Result',comb_image)
cv2.waitKey(0)







