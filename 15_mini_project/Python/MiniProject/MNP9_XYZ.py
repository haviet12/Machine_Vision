import cv2
import numpy as np
from PIL import Image



file_hinh=r'MiniProject\Lenna_(test_image).jpg'
original_img = cv2.imread(file_hinh)
img_PIL = Image.open(file_hinh)

def Cvt2XYZ(img):
    list=[]
    #create 4 image C, M, Y, K
    XYZ_img = Image.new(img.mode, img.size)
    X_img = Image.new(img.mode, img.size)
    Y_img = Image.new(img.mode, img.size)
    Z_img = Image.new(img.mode, img.size)

    # get size of original_img
    height = img.size[0]
    width = img.size[1]
    for x in range(height):
        for y in range(width):
            # get pixel at point (x,y)
            r,g,b = img_PIL.getpixel((x, y))
            X = np.uint8(0.4124564 * r + 0.3575761 * g + 0.1804375 * b)
            Y = np.uint8(0.2126729 * r + 0.7151522 * g + 0.0721750 * b)
            Z = np.uint8(0.0193339 * r + 0.1191920 * g + 0.9503041 * b)

            # set pixel
            XYZ_img.putpixel((x,y), (Z,Y,X))        
            X_img.putpixel((x,y), (X,X,X))          
            Y_img.putpixel((x,y), (Y,Y,Y))
            Z_img.putpixel((x,y),(Z,Z,Z))
    xyz_img =np.array(XYZ_img)
    x_img= np.array(X_img)
    y_img= np.array(Y_img)
    z_img= np.array(Z_img)

    list.append(xyz_img)
    list.append(x_img)
    list.append(y_img)
    list.append(z_img)

    return list

img =img_PIL

color=Cvt2XYZ(img)
           #convert image to array (show image by opencv)

# show image
cv2.imshow("HINH GOC", original_img)
cv2.imshow("Kenh Mau XYZ", color[0])
cv2.imshow("Kenh Mau X", color[1])
cv2.imshow("Kenh Mau Y", color[2])
cv2.imshow("Kenh Mau Z", color[3])

cv2.waitKey(0)
cv2.destroyAllWindows()
