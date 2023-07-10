import cv2
import numpy as np
from PIL import Image
from math import *

file_hinh= r'MiniProject\Lenna_(test_image).jpg'

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

    #anh_xam =np.array(average_img)
    return average_img

def EdgeDetection(img,threshold):
    new_img= Image.new(img.mode,img.size)
    Sx = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    Sy= np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
 
    for x in range(1,img.size[0]-2):
        for y in range(1,img.size[1]-2):
            GRx=0
            GGx=0 
            GBx=0
            GRy=0
            GGy=0
            GBy=0
            Gxx=0
            Gyy=0
            Gxy=0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    Gr,Gg,Gb = img.getpixel((i,j))
                    ## kênh Red
                    GRx+=int(Gr*Sx[i-x+1,j-y+1])
                    GRy+=int(Gr*Sy[i-x+1,j-y+1])
                    ## kênh Green
                    GGx+=int(Gg*Sx[i-x+1,j-y+1])
                    GGy+=int(Gg*Sy[i-x+1,j-y+1])
                    ## kênh Blue
                    GBx+=int(Gb*Sx[i-x+1,j-y+1])
                    GBy+=int(Gb*Sy[i-x+1,j-y+1])
            
            ## tính các giá trị Gxx Gyy Gxy

            Gxx= pow(GRx,2) + pow(GGx,2) + pow(GBx,2)
            Gyy= pow(GRy,2) + pow(GGy,2) + pow(GBy,2)
            Gxy = GRx*GRy +GGx*GGy +GBy*GBx

            ## tính giá trị theta
            theta =int( 0.5*atan2(2*Gyy,(Gxx-Gyy)))
            
            Fxy =int(sqrt(0.5*((Gxx+Gyy)+(Gxx-Gyy)*cos(2*theta)+2*Gxy*sin(2*theta))))
            if Fxy>= threshold:
                new_img.putpixel((x,y),(0,0,0))
            else:
                new_img.putpixel((x,y),(255,255,255))
    dis_img= np.array(new_img)
    return dis_img


##### goi ham con
hinh_goc=cv2.imread(file_hinh)
img_pil=Image.open(file_hinh)

gray_img =lightness_img(img_pil)
threshold = int(input('threshold: '))


img_displayed = EdgeDetection(gray_img,threshold)
##### show hinh

cv2.imshow("hinh goc", hinh_goc)
cv2.imshow("Egde Detection Image",img_displayed)

cv2.waitKey(0)
cv2.destroyAllWindows()

