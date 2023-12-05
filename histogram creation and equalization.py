import matplotlib.pyplot as plt
import numpy as np
import cv2

x=cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)
cv2.imshow(winname="input", mat=x)
height=x.shape[0]
width=x.shape[1]
hist={}
for i in range(0,256):
    hist[i]=0

intensities= list(hist.keys())
for i in range(height):
    for j in range(width):
        val=x[i,j]
        hist[val]+=1

values= list(hist.values())
plt.figure(figsize=(6,6))
plt.bar(intensities,values)
plt.title('Self')

hist1=cv2.calcHist([x],[0], None, [256], [0,256])
hist1=np.squeeze(hist1)
plt.figure(figsize=(6,6))
plt.bar(intensities,hist1)
plt.title('Inbuilt')

prob={}
for i in range(0,256):
    prob[i]=values[i]/(height*width)

probability=list(prob.values())
mapped_to={}
for i in range(0,256):
    y=sum(probability[0:i+1])
    mapped_to[i]=int(255*y)

output=np.zeros_like(x)
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        ele=x[i,j]
        output[i,j]=mapped_to[ele]

cv2.imshow(winname='output', mat=output)
plt.show()
cv2.waitKey(0)