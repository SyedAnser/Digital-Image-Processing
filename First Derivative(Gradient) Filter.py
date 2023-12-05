import matplotlib.pyplot as plt
import numpy as np
import cv2

x=cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)
cv2.imshow(winname="intput", mat=x)

height=x.shape[0]
width=x.shape[1]
input=np.zeros_like(x)

input=cv2.copyMakeBorder(x,1,1,1,1,cv2.BORDER_REFLECT,input)
output=np.zeros_like(x)

for a in range(height):
    for b in range(width):
        gx=abs(input[a+1,b]-input[a,b])
        gy=abs(input[a,b+1]-input[a,b])
        output[a,b]=gx+gy



cv2.imshow(winname="output", mat=output)

cv2.waitKey(0)