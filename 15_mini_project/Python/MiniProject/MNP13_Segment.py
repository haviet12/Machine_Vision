import cv2
import numpy as np
from PIL import Image
from math import *

file_hinh= r'MiniProject\Lenna_(test_image).jpg'
x1= int(input(' nhap toa do x1: '))
y1= int(input(' nhap toa do y1: '))
x2= int(input(' nhap toa do x2: '))
y2= int(input(' nhap toa do y2: '))
threshold = int(input(' threshold: '))
hinh_goc=cv2.imread(file_hinh)
img_pil=Image.open(file_hinh)
width= img_pil.size[0]
height= img_pil.size[1]

new_img = Image.new(img_pil.mode, img_pil.size)
### tính tổng giá trị các điểm ảnh từ (x1,y1) đến (x2,y2)
Rn=0
Gn=0
Bn=0

for i in range (x1,x2):
    for j in range (y1,y2):
        Red,Green,Blue = img_pil.getpixel((i,j))

        Rn += Red
        Gn+= Green
        Bn+= Blue

size = (abs(x1-x2)*abs(y1-y2))
Rn/= size
Gn/= size
Bn/= size

### tính giá trị Euclidean distance và so sánh với ngưỡng
D=0
for x in range(width):
    for y in range(height):
        Zr,Zg,Zb=img_pil.getpixel((x,y))
        D = sqrt((Zr-Rn)*(Zr-Rn)+(Zg-Gn)*(Zg-Gn)+(Zb-Bn)*(Zb-Bn))
        
        if D<=threshold:
            new_img.putpixel((x,y),(255,255,255))
        else:
            new_img.putpixel((x,y),(Zb,Zg,Zr))
img_dis= np.array(new_img)

### show len man hinh
cv2.imshow('Hinh Goc', hinh_goc)
cv2.imshow('Hinh Segmentation',img_dis)

cv2.waitKey(0)
cv2.destroyAllWindows()


