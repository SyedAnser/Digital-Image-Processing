import matplotlib.pyplot as plt
import numpy as np
import cv2

x=cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)
cv2.imshow(winname="intput", mat=x)

height=x.shape[0]
width=x.shape[1]
input=np.zeros_like(x)

input=cv2.copyMakeBorder(x,1,1,1,1,cv2.BORDER_REFLECT,input)

# filter=np.array([[1,1,1],
#                  [1,1,1],
#                  [1,1,1]])

# h1=filter.shape[0]
# w1=filter.shape[1]
# output=np.zeros_like(x)
# for a in range(height):
#     for b in range(width):
#         sum=0
#         for i in range(h1):
#             for j in range(w1):
#                 sum+=input[a+i,b+j]*filter[i,j]
#         output[a,b]=sum/9

# cv2.imshow(winname="output", mat=output)
# y=cv2.blur(x,(3,3))
# cv2.imshow(winname="inbuilt", mat=y)

filter=np.array([[1,2,1],
                 [2,4,2],
                 [1,2,1]])

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
        output1[a,b]=sum/16

for a in range(height):
    for b in range(width):
        sum=0
        for i in range(h1):
            for j in range(w1):
                sum+=input[a-i,b-j]*filter[i,j]
        output2[a,b]=sum/16

cv2.imshow(winname="corr", mat=output1)
cv2.imshow(winname="conv", mat=output1)

y=cv2.blur(x,(3,3))
cv2.imshow(winname="inbuilt", mat=y)

cv2.waitKey(0)
