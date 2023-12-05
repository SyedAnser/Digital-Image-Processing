import numpy as np
import cv2

x=cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)
cv2.imshow(winname="intput", mat=x)

height=x.shape[0]
width=x.shape[1]
input=np.zeros_like(x)

input=cv2.copyMakeBorder(x,1,1,1,1,cv2.BORDER_REFLECT,input)

filter=np.array([[0,1,0],
                 [1,-4,1],
                 [0,1,0]])

h1=filter.shape[0]
w1=filter.shape[1]
output1=np.zeros_like(x)
output2=np.zeros_like(x)

for a in range(height):
    for b in range(width):
        sum=0
        for i in range(h1):
            for j in range(w1):
                sum+=input[a+i,b+j]*filter[i,j]
        output2[a,b]=sum

fm=output2-np.min(output2)
fs=255*(fm/np.max(fm))
fs=np.uint8(fs)
output1=x+fs
cv2.imshow(winname="laplacian", mat=fs)


cv2.waitKey(0)