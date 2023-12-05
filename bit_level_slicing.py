import numpy as np
import cv2

image_path = "C:/Users/syeda/OneDrive/Desktop/codes/DIP/lena.png"

# Read the saved image using OpenCV
loaded_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform bit-level slicing and create a list to store result images
bit_planes = []
for i in range(8):
    bit_plane = (loaded_image >> i) & 1
    bit_planes.append(bit_plane * 255)

# Add the original image to the list
bit_planes.append(loaded_image)

# Display all 9 images (bit planes and original)
for i, image in enumerate(bit_planes):
    cv2.imshow(f"Bit Plane {i+1}", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
