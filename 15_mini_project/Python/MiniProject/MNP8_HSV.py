import cv2
import numpy as np
from PIL import Image
from math import *


file_hinh=r'MiniProject\Lenna_(test_image).jpg'
original_img = cv2.imread(file_hinh)
img_PIL = Image.open(file_hinh)

def Cvt2HSI(img):
    HSV=[]
    #create 4 image C, M, Y, K
    HSI_img = Image.new(img.mode, img.size)
    H_img = Image.new(img.mode, img.size)
    S_img = Image.new(img.mode, img.size)
    V_img = Image.new(img.mode, img.size)

    # get size of original_img
    height = img.size[0]
    width = img.size[1]
    for x in range(height):
        for y in range(width):
            # get pixel at point (x,y)
            r,g,b = img_PIL.getpixel((x, y))
      
            t1=(0.5*((r-g)+(r-b)))
            t2=((r-g)*(r-g)+(r-b)*(g-b))
            t3=(sqrt(t2))
            theta = acos(t1/t3)
            
            if b<=g:
                H=np.uint8( theta)
            else:
                H=np.uint8(360-theta*180/pi)
            # tính gái trị của S ( saturation)
            a= 1-3/(r+g+b)
            b = min(r,g,b)
            S = np.uint8(a*b*255)
           
           
            # tính giá trị của I ( intensity)
            V= max(r,g,b)

            # set pixel
            HSI_img.putpixel((x,y), (V,S,H))        
            H_img.putpixel((x,y), (H,H,H))          
            S_img.putpixel((x,y), (S,S,S))
            V_img.putpixel((x,y),(V,V,V))
    hsi_img =np.array(HSI_img)
    h_img= np.array(H_img)
    s_img= np.array(S_img)
    v_img= np.array(V_img)

    HSV.append(hsi_img)
    HSV.append(h_img)
    HSV.append(s_img)
    HSV.append(v_img)

    return HSV

img =img_PIL

color=Cvt2HSI(img)
           #convert image to array (show image by opencv)

# show image
cv2.imshow("HINH GOC", original_img)
cv2.imshow("Kenh Mau HSI", color[0])
cv2.imshow("Kenh Mau H", color[1])
cv2.imshow("Kenh Mau S", color[2])
cv2.imshow("Kenh Mau V", color[3])

cv2.waitKey(0)
cv2.destroyAllWindows()
