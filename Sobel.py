import numpy as np
import cv2

x=cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)
cv2.imshow(winname="intput", mat=x)

height=x.shape[0]
width=x.shape[1]
input=np.zeros_like(x)

input=cv2.copyMakeBorder(x,1,1,1,1,cv2.BORDER_REFLECT,input)


filter_x=np.array([[-1,-1,-1],
                 [0,0,0],
                 [1,1,1]])

filter_y=np.array([[-1,0,1],
                 [-1,0,1],
                 [-1,0,1]])

output2=np.zeros_like(x)
h1=filter_x.shape[0]
w1=filter_x.shape[1]

for a in range(height):
    for b in range(width):
        sum_x=0
        sum_y=0
        for i in range(h1):
            for j in range(w1):
                sum_x+=input[a+i,b+j]*filter_x[i,j]
                sum_y+=input[a+i,b+j]*filter_y[i,j]
        output2[a,b]=abs(sum_x)+abs(sum_y)
        

fm=output2-np.min(output2)
fs=255*(fm/np.max(fm))
fs=np.uint8(fs)
cv2.imshow(winname="prewitt", mat=fs)

filter_x=np.array([[-1,-2,-1],
                 [0,0,0],
                 [1,2,1]])

filter_y=np.array([[-1,0,1],
                 [-2,0,2],
                 [-1,0,1]])

output2=np.zeros_like(x)
h1=filter_x.shape[0]
w1=filter_x.shape[1]

for a in range(height):
    for b in range(width):
        sum_x=0
        sum_y=0
        for i in range(h1):
            for j in range(w1):
                sum_x+=input[a+i,b+j]*filter_x[i,j]
                sum_y+=input[a+i,b+j]*filter_y[i,j]
        output2[a,b]=abs(sum_x)+abs(sum_y)
        

fm=output2-np.min(output2)
fs=255*(fm/np.max(fm))
fs=np.uint8(fs)
cv2.imshow(winname="sobel", mat=fs)

cv2.waitKey(0)