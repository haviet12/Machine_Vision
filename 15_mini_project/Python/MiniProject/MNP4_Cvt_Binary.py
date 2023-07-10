import cv2
import numpy as np
from PIL import Image
from math import *

file_img =r'MiniProject\Lenna_(test_image).jpg'
img_display= cv2.imread(file_img)

img = Image.open(file_img)
def luminance_img(img):
    average_img = Image.new(img.mode, img.size)
    height = average_img.size[1]
    width = average_img.size[0]
    for x in range(width):
        for y in range(height):
            R,G,B = img.getpixel((x,y))
            gray = np.uint8(0.2126*R+0.7152*G+0.0722*B)
            average_img.putpixel((x,y),(gray,gray,gray))

    ## chuyển ảnh từ PIL sang opencv để hiển thị 

    anh_xam =np.array(average_img)
    return anh_xam  

def binary_img(img, threshold):
    binary_img = Image.new(img.mode, img.size)
    height = binary_img.size[1]
    width =  binary_img.size[0]
    for x in range(width):
        for y in range(height):
            R,G,B = img.getpixel((x,y))
            gray = np.uint8(0.2126*R+0.7152*G+0.0722*B)

            if gray<threshold:
                gray =0
            else:
                gray=255
            binary_img.putpixel((x,y),(gray,gray,gray))

    ## chuyển ảnh từ PIL sang opencv để hiển thị 

    anh_xam =np.array( binary_img)
    return anh_xam 
threshold = int(input('Threshold = '))
cv2.imshow('HINH GOC', img_display)
cv2.imshow('Gray_Img_Luminance',luminance_img(img))
cv2.imshow(f"Anh Nhi Phan Nguong {threshold}",binary_img(img, threshold))
cv2.waitKey(0)
cv2.destroyAllWindowss()