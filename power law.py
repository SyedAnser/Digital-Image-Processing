import cv2
import numpy as np
img_input=cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)
img=15*img_input**0.3
img_output=img.astype(np.uint8)
cv2.imshow(winname='input', mat=img_input)
cv2.imshow(winname='power', mat=img_output)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite(img_output, filename='power law transformed img' )
    cv2.destroyAllWindows()