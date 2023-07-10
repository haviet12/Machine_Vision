import cv2
import numpy as np
from PIL import Image



file_hinh=r'MiniProject\Lenna_(test_image).jpg'
original_img = cv2.imread(file_hinh)
img_PIL = Image.open(file_hinh)

def Cvt2YCbCr(img):
    list=[]
    #create 4 image C, M, Y, K
    YCbCr_img = Image.new(img.mode, img.size)
    Y_img = Image.new(img.mode, img.size)
    Cr_img = Image.new(img.mode, img.size)
    Cb_img = Image.new(img.mode, img.size)

    # get size of original_img
    height = img.size[0]
    width = img.size[1]
    for x in range(height):
        for y in range(width):
            # get pixel at point (x,y)
            R,G,B = img_PIL.getpixel((x, y))
            Y = np.uint8(16+(65.738*R/256)+(129.057*G/256)+(25.064*B/256))
            Cb =np.uint8( 128 - (37.945 * R / 256) - (74.494 * G / 256) + (112.439 * B / 256))
            Cr =np.uint8( 128 + (112.439 * R / 256) - (94.154 * G / 256) - (18.285 * B / 256))
            # set pixel
            YCbCr_img.putpixel((x,y), (Cr,Cb,Y))        
            Y_img.putpixel((x,y), (Y,Y,Y))          
            Cb_img.putpixel((x,y), (Cb,Cb,Cb))
            Cr_img.putpixel((x,y),(Cr,Cr,Cr))
    a =np.array(YCbCr_img)
    b= np.array(Y_img)
    c= np.array(Cb_img)
    d= np.array(Cr_img)

    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)

    return list

img =img_PIL

color=Cvt2YCbCr(img)
           #convert image to array (show image by opencv)

# show image
cv2.imshow("HINH GOC", original_img)
cv2.imshow("Kenh Mau YCbCr", color[0])
cv2.imshow("Kenh Mau Y", color[1])
cv2.imshow("Kenh Mau Cb", color[2])
cv2.imshow("Kenh Mau Cr", color[3])

cv2.waitKey(0)
cv2.destroyAllWindows()
