import cv2
import numpy as np

x=cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/DIP/lena.png")
h,w,c=x.shape
r = np.zeros_like(x)
g = np.zeros_like(x)
b = np.zeros_like(x)



for p in range(h):
    for q in range(w):
        r[p, q] = x[p, q, 2]  # Red channel
        g[p, q] = x[p, q, 1]  # Green channel
        b[p, q] = x[p, q, 0]  # Blue channel

       
cv2.imshow(winname='Input', mat=x)
   
cv2.imshow(winname='Gamma 0.5', mat=r)
cv2.imshow(winname='Gamma 1', mat=g)
cv2.imshow(winname='Gamma 2', mat=b)

cv2.waitKey(0)