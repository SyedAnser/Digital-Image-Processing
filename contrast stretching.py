
import cv2
import numpy as np
 
img_input = cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)
 
img_output = np.zeros_like(img_input)
 
for i in range(img_input.shape[0]):
    for j in range(img_input.shape[1]):
        img_output[i,j] = 255*(img_input[i,j]-(np.min(img_input)))/((np.max(img_input))-(np.min(img_input)))
 
cv2.imshow(winname='input', mat=img_input)
cv2.imshow(winname='contrast', mat=img_output)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite(img_output, filename='contrast strateched img' )
    cv2.destroyAllWindows()