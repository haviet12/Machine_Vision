from tkinter import *
import cv2
import numpy as np
from PIL import Image

frame=Tk()
frame.geometry('400x500')


file_hinh=r'MiniProject\Lenna_(test_image).jpg'
original_img = cv2.imread(file_hinh)
img_PIL = Image.open(file_hinh)

height = img_PIL.size[0]
width = img_PIL.size[1]


def Smooth_3x3 (img):
    new_img = Image.new(img.mode, img.size)
    for x in range (1, width-1):
        for y in range (1, height-1):
            Rs=0
            Gs=0
            Bs=0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    R,G,B =img.getpixel((i,j))

                    Rs = Rs +R
                    Gs = Gs +G
                    Bs = Bs +B
                
            K=3*3 
            Rs=np.uint8( Rs/K)
            Gs=np.uint8(Gs/K)
            Bs=np.uint8(Bs/K)
         
            new_img.putpixel((x,y),(Bs,Gs,Rs))
            display_img =np.array(new_img)
    return display_img


cv2.imshow("Hinh Goc", original_img)
cv2.imshow("Smooth_Img_3x3",Smooth_3x3(img_PIL))
cv2.waitKey(0)
cv2.destroyAllWindows()
                    