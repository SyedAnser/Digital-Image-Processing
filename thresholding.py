import cv2
import numpy as np
img_input=cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)
above=img_input>125
print(above)
img_output=np.zeros_like(img_input)
img_output[above]=255
cv2.imshow(winname='input', mat=img_input)
cv2.imshow(winname='threshold', mat=img_output)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite(img_output, filename='thresholded img' )
    cv2.destroyAllWindows()