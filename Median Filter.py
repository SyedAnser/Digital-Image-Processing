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
        sum=[]
        for i in range(3):
            for j in range(3):
                sum.append(input[a+i,b+j])
                sum.sort()
        output[a,b]=sum[5]

cv2.imshow(winname="output", mat=output)
y=cv2.medianBlur(x,3)
cv2.imshow(winname="inbuilt", mat=y)
cv2.waitKey(0)