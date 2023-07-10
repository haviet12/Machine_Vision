import cv2
import numpy as np

original_img= cv2.imread("MiniProject\Lenna_(test_image).jpg")

red = np.zeros(original_img.shape,np.uint8)
green = np.zeros(original_img.shape,np.uint8)
blue = np.zeros(original_img.shape,np.uint8)

(height,width, channels) = original_img.shape

# red[:]=[0,0,0]
# green[:]=[0,0,0]
# blue[:]=[0,0,0]
for i in range(height):
    for j in range(width):
        R = original_img[i,j,2]
        G = original_img[i,j,1]
        B = original_img[i,j,0] 

        red[i,j,2]=R
        green[i,j,1]=G
        blue[i,j,0]=B


cv2.imshow("Hinh_Goc",original_img)
cv2.imshow("Kenh_RED",red)
cv2.imshow("Kenh_GREEN",green)
cv2.imshow("Kenh_BLUE",blue)
cv2.waitKey(0)
cv2.destroyAllWindows()
