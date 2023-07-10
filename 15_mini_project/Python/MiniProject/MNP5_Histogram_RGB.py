import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

file_hinh =r"MiniProject\bird_small.jpg"

original_img= cv2.imread(file_hinh)

# open by PIL
img = Image.open(file_hinh)
# convert image -> Grayscale


def calc_histogram (img):
    histogram = np.zeros((256,3))
    height = img.size[1]
    width = img.size[0]
    for x in range(width):
        for y in range(height):
            R,G,B = img.getpixel((x,y))
            histogram[R,2]+=1
            histogram[G,1]+=1
            histogram[B,0]+=1

    return histogram

def draw_histogram(data):
    W=5
    H=4
    plt.figure('Histogram_chart', figsize=(((W,H))), dpi=150)
    trucX = np.zeros(256)
    trucX=np.linspace(0,256,256)
    plt.plot(trucX, data, color='orange')
    plt.suptitle("Histogram Chart")
    plt.xlabel('pixel')
    plt.ylabel('số pixel giống nhau')
    plt.show()
        
# chuyen hinh anh tu PIL ve OPENCV de hien thi


# hien thi anh
cv2.imshow("HINH GOC", original_img)


#goi cac ham con 

data =calc_histogram(img)
draw_histogram(data)

# cv2.imshow("Grayscale", lightness_img(img))
cv2.waitKey(0)
cv2.destroyAllWindows()