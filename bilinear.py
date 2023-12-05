import numpy as np

def bilinear_interpolation(input_image, output_shape):
    input_height, input_width = input_image.shape
    output_height, output_width = output_shape
    
    height_ratio = (input_height - 1) / (output_height - 1)
    width_ratio = (input_width - 1) / (output_width - 1)
    
    output_image = np.zeros(output_shape, dtype=input_image.dtype)
    
    for y_out in range(output_height):
        for x_out in range(output_width):
            y_in = y_out * height_ratio
            x_in = x_out * width_ratio
            
            y_in_floor = int(np.floor(y_in))
            y_in_ceil = int(np.ceil(y_in))
            x_in_floor = int(np.floor(x_in))
            x_in_ceil = int(np.ceil(x_in))
            
            y_weight = y_in - y_in_floor
            x_weight = x_in - x_in_floor
            
            top_left = input_image[y_in_floor, x_in_floor]
            top_right = input_image[y_in_floor, x_in_ceil]
            bottom_left = input_image[y_in_ceil, x_in_floor]
            bottom_right = input_image[y_in_ceil, x_in_ceil]
            
            top_interpolation = top_left * (1 - x_weight) + top_right * x_weight
            bottom_interpolation = bottom_left * (1 - x_weight) + bottom_right * x_weight
            
            output_image[y_out, x_out] = top_interpolation * (1 - y_weight) + bottom_interpolation * y_weight
    
    return output_image

input_image = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

output_height = 6
output_width = 6

output_image = bilinear_interpolation(input_image, (output_height, output_width))

print("Input Image:")
print(input_image)
print("\nOutput Image (Bilinear Interpolation):")
print(output_image)
