import numpy as np

def translate_image(input_image, translation):
    translation_matrix = np.array([[1, 0, -translation[0]],
                                   [0, 1, -translation[1]],
                                   [0, 0, 1]])
    
    output_image = np.zeros_like(input_image)
    
    for x_out in range(output_image.shape[0]):
        for y_out in range(output_image.shape[1]):
            translated_coords = np.dot(translation_matrix, [x_out, y_out, 1])
            x_in = int(translated_coords[0])
            y_in = int(translated_coords[1])
            
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

translation = (2, 2)

output_image = translate_image(input_image, translation)

print("Input Image:")
print(input_image)
print("\nOutput Image (Translated):")
print(output_image)
