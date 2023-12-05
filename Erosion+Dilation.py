import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/DIP/pic1.png",0)


kernel = np.ones(shape=(3,3),dtype='uint8')


print(kernel)

def custom_erosion(image, filter):
    result = np.zeros_like(image)
    k_height, k_width = filter.shape
    kernel_shape = k_height // 2, k_width // 2

    for y in range(kernel_shape[0], image.shape[0] - kernel_shape[0]):
        for x in range(kernel_shape[1], image.shape[1] - kernel_shape[1]):
            region = image[y - kernel_shape[0]:y + kernel_shape[0] + 1, x - kernel_shape[1]:x + kernel_shape[1] + 1]
            result[y, x] = np.min(region * filter)

    return result

def custom_dilation(image, kernel):
    result = np.zeros_like(image)
    k_height, k_width = kernel.shape
    kernel_shape = k_height // 2, k_width // 2

    for y in range(kernel_shape[0], image.shape[0] - kernel_shape[0]):
        for x in range(kernel_shape[1], image.shape[1] - kernel_shape[1]):
            region = image[y - kernel_shape[0]:y + kernel_shape[0] + 1, x - kernel_shape[1]:x + kernel_shape[1] + 1]
            result[y, x] = np.max(region * kernel)

    return result

erosion = custom_erosion(image, kernel)
dilation = custom_dilation(image, kernel)

boundary_extraction=image-erosion

cv2.imshow(winname='binary',mat=image)
cv2.imshow(winname='erosion',mat=erosion)
cv2.imshow(winname='dilation',mat=dilation)
cv2.imshow(winname='boundary extraction',mat=boundary_extraction)


cv2.waitKey(0)
