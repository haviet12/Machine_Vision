import cv2
import numpy as np
from PIL import Image
from math import *

file_hinh= r'MiniProject\Lenna_(test_image).jpg'

img_cv2=cv2.imread(file_hinh)
img_pil= Image.open(file_hinh)

def sharp_img (img):
    new_img = Image.new(img.mode, img.size)
    matrix = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    for x in range (1, img.size[0]-2):
        for y in range (1, img.size[1]-2):
            Rn =0
            Gn=0
            Bn=0
            for i in range (x-1,x+2):
                for j in range (y-1,y+2):
                    Red,Green,Blue = img.getpixel((i, j))
                    Rn+=int( Red*matrix[i-x+1,j-y+1])
                    Gn+= int(Green*matrix[i-x+1,j-y+1])
                    Bn+= int(Blue*matrix[i-x+1,j-y+1])
            
            R,G,B=img.getpixel((x,y))
            Rn = abs(R)+abs(Rn)
            Gn = abs(G)+abs(Gn)
            Bn = abs(B)+abs(Bn)

            if Rn< 0:
                Rn=0
            elif Rn>255:
                Rn=255
            if  Gn<0:
                Gn=0
            elif Gn>255: Gn=255

            if Bn<0:
                Bn=0
            elif Bn>255 : Bn=255
            new_img.putpixel((x,y),(Bn,Gn,Rn))
    img_dis = np.array(new_img)
    return img_dis

cv2.imshow(' Hinh goc', img_cv2)
cv2.imshow("Sharping Image",sharp_img(img_pil))

cv2.waitKey(0)
cv2.destroyAllWindows()