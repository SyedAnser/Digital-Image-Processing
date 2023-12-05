import cv2
import numpy as np

img = cv2.imread("C:/Users/syeda/OneDrive/Desktop/codes/lena_gray.jpg",0)

def flipvertical():
    height, width = img.shape
    img_output = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            img_output[i][j] = img[height-i-1][width-j-1]
            

    cv2.imshow("flip.png", img_output)

    cv2.imshow("Input", img)

    while 1:
        key = cv2.waitKey(0)
        if key == 27:
            cv2.destroyAllWindows()
            break
        elif key == ord('d'):
            cv2.destroyAllWindows()
            cv2.imshow("Output", img_output)
        elif key == ord('a'):
            cv2.destroyAllWindows()
            cv2.imshow("Input", img)

def main():
    flipvertical()

if __name__ == "__main__":
    main()