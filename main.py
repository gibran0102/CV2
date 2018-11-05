import numpy as np 
import cv2 

def main():
    img = cv2.imread('img.png', 0)
    cv2.imshow('image', img)
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('copy.png', img)
        cv2.destroyAllWindows()

if __name__ == '__main__': main()

