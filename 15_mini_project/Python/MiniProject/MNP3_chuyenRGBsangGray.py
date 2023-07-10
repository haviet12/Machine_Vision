import cv2
import numpy as np
from PIL import Image
from math import *
img_display= cv2.imread('MiniProject\Lenna_(test_image).jpg')


## đọc file bằng hàn Image của PIL

img = Image.open('MiniProject\Lenna_(test_image).jpg')
def lightness_img(img):
## tạo ra 1 ảnh mới với cùng chế độ và size của img
    average_img = Image.new(img.mode, img.size)
    height = average_img.size[1]
    width = average_img.size[0]
    for x in range(width):
        for y in range(height):
            R,G,B = img.getpixel((x,y))
            # value_color = [R,G,B]
            # max(R,G,B)
            # min(R,G,B)
            gray = np.uint8((max(R,G,B) +min(R,G,B))/2)
            average_img.putpixel((x,y),(gray,gray,gray))

    ## chuyển ảnh từ PIL sang opencv để hiển thị 

    anh_xam =np.array(average_img)
    return anh_xam

def average_img(img):
    average_img = Image.new(img.mode, img.size)
    height = average_img.size[1]
    width = average_img.size[0]
    for x in range(width):
        for y in range(height):
            R,G,B = img.getpixel((x,y))
            gray = np.uint8((R+G+B)/3)
            average_img.putpixel((x,y),(gray,gray,gray))

    ## chuyển ảnh từ PIL sang opencv để hiển thị 

    anh_xam =np.array(average_img)
    return anh_xam

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


cv2.imshow('Nguyen_Viet_ha_20146489',img_display)
cv2.imshow('Gray_Img_Average',average_img(img))
cv2.imshow('Gray_Img_Ligghtness',lightness_img(img))
cv2.imshow('Gray_Img_Luminance',luminance_img(img))
cv2.waitKey(0)
cv2.destroyAllWindowss()