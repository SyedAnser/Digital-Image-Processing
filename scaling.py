import numpy as np

def scale_image(input_image, scaling_factor):
    scaling_matrix = np.array([[1/scaling_factor, 0, 0],
                               [0, 1/scaling_factor, 0],
                               [0, 0, 1]])
    
    output_height = input_image.shape[0]
    output_width = input_image.shape[1]
    
    center_y = input_image.shape[0] // 2
    center_x = input_image.shape[1] // 2
    
    output_image = np.zeros((output_height, output_width), dtype=input_image.dtype)
    
    for y_out in range(output_height):
        for x_out in range(output_width):
            y_in_centered = y_out - center_y
            x_in_centered = x_out - center_x
            
            scaled_coords = np.dot(scaling_matrix, [y_in_centered, x_in_centered, 1])
            y_in = int(scaled_coords[0] + center_y)
            x_in = int(scaled_coords[1] + center_x)
            
            if 0 <= y_in < input_image.shape[0] and 0 <= x_in < input_image.shape[1]:
                output_image[y_out, x_out] = input_image[y_in, x_in]
    
    return output_image

input_image = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],])

scaling_factor = 2

output_image = scale_image(input_image, scaling_factor)

print("Input Image:")
print(input_image)
print("\nOutput Image (Scaled with Center Zoom):")
print(output_image)
