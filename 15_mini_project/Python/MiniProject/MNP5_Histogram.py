
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


     

file_hinh =r"MiniProject\bird_small.jpg"

original_img= cv2.imread(file_hinh)

# open by PIL
img = Image.open(file_hinh)
# convert image -> Grayscale

def lightness_img(img):
## tạo ra 1 ảnh mới với cùng chế độ và size của img
     
    average_img = Image.new(img.mode, img.size)
    height = average_img.size[1]
    width = average_img.size[0]
    for x in range(width):
        for y in range(height):
            R,G,B = img.getpixel((x,y))
           
            gray = np.uint8((max(R,G,B) +min(R,G,B))/2)
            average_img.putpixel((x,y),(gray,gray,gray))

    ## chuyển ảnh từ PIL sang opencv để hiển thị 
    return average_img

def calc_histogram (hinh_xam_PIL):
    histogram = np.zeros(256)
    height = hinh_xam_PIL.size[1]
    width = hinh_xam_PIL.size[0]
    for x in range(width):
        for y in range(height):
            R,G,B = hinh_xam_PIL.getpixel((x,y))
            histogram[R]+=1

    return histogram

def draw_histogram(data):
    W=5
    H=4
    plt.figure('Histogram_chart', figsize=(((W,H))), dpi=150)
    trucX = np.zeros(256)
    trucX=np.linspace(0,256,256)
    plt.plot(trucX, data, color='black')
    plt.suptitle("Histogram Chart")
    plt.xlabel('pixel')
    plt.ylabel('số pixel giống nhau')
    plt.show()
        
# chuyen hinh anh tu PIL ve OPENCV de hien thi
gray_display= np.array(lightness_img(img))

# hien thi anh
cv2.imshow("HINH GOC", original_img)
cv2.imshow("Gray Scale", gray_display)

#goi cac ham con 
hinh_xam_PIL= lightness_img(img)
data =calc_histogram(hinh_xam_PIL)
draw_histogram(data)

# cv2.imshow("Grayscale", lightness_img(img))
cv2.waitKey(0)
cv2.destroyAllWindows()