import numpy as np
import matplotlib.pyplot as plt
import math

def rotate_matrix(input_matrix, angle_deg):
    angle_rad = math.radians(angle_deg)
    
    input_height, input_width = input_matrix.shape
    
    center_y = input_height // 2
    center_x = input_width // 2
    
    rotation_matrix = np.array([[math.cos(angle_rad), math.sin(angle_rad), 0],
                                [-math.sin(angle_rad), math.cos(angle_rad), 0],
                                [0, 0, 1]])
    
    translation1_matrix = np.array([[1, 0, -center_x],
                                   [0, 1, -center_y],
                                   [0, 0, 1]])
    
    translation2_matrix = np.array([[1, 0, center_x],
                                   [0, 1, center_y],
                                   [0, 0, 1]])
    
    output_matrix = np.zeros((input_height, input_width), dtype=input_matrix.dtype)
    
    for y_out in range(input_height):
        for x_out in range(input_width):
            rotated_coords = np.dot(translation2_matrix, np.dot(rotation_matrix, np.dot(translation1_matrix, [y_out, x_out, 1])))
            y_in = int(rotated_coords[0])
            x_in = int(rotated_coords[1])
            
            if 0 <= y_in < input_height and 0 <= x_in < input_width:
                output_matrix[y_out, x_out] = input_matrix[y_in, x_in]
    
    return output_matrix

input_matrix = np.zeros((8, 8), dtype=np.uint8)
input_matrix[3:5, 2:6] = 1  

angle_deg = 45

output_matrix = rotate_matrix(input_matrix, angle_deg)

print("Input Matrix:")
print(input_matrix)
print("\nOutput Matrix (Rotated):")
print(output_matrix)
