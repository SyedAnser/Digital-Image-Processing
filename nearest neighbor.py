import numpy as np

def nearest_neighbor_interpolation_n8(input_image, output_shape):
    input_height, input_width = input_image.shape
    output_height, output_width = output_shape
    
    height_ratio = input_height / output_height
    width_ratio = input_width / output_width
    
    output_image = np.zeros(output_shape, dtype=input_image.dtype)
    
    for y_out in range(output_height):
        for x_out in range(output_width):
            y_in = int(y_out * height_ratio)
            x_in = int(x_out * width_ratio)
            
            nearest_neighbors = [
                (y_in, x_in), 
                (y_in - 1, x_in),
                (y_in + 1, x_in),
                (y_in, x_in - 1),
                (y_in, x_in + 1),
                (y_in - 1, x_in - 1),
                (y_in - 1, x_in + 1),
                (y_in + 1, x_in - 1),
                (y_in + 1, x_in + 1)
            ]
            
            valid_neighbors = [(y, x) for y, x in nearest_neighbors if 0 <= y < input_height and 0 <= x < input_width]
            neighbor_values = [input_image[y, x] for y, x in valid_neighbors]
            output_image[y_out, x_out] = min(neighbor_values, key=lambda val: abs(val - input_image[y_in, x_in]))
    
    return output_image

input_image = np.array([[0, 1, 0],
                        [1, 1, 1],
                        [0, 1, 0]])

output_height = 5
output_width = 5

output_image = nearest_neighbor_interpolation_n8(input_image, (output_height, output_width))

print("Input Image:")
print(input_image)
print("\nOutput Image (N8 Nearest Neighbor Interpolation):")
print(output_image)
