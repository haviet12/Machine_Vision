import cv2
import numpy as np
from PIL import Image
# read image
file_hinh= r'MiniProject\Lenna_(test_image).jpg'
original_img = cv2.imread(file_hinh)
img_PIL = Image.open(file_hinh)

def Cvt2CMYK(img):
    CMYK=[]
    #create 4 image C, M, Y, K
    C = Image.new(img.mode, img.size)
    M = Image.new(img.mode, img.size)
    Y = Image.new(img.mode, img.size)
    K = Image.new(img.mode, img.size)

    # get size of original_img
    height = img.size[0]
    width = img.size[1]
    for x in range(height):
        for y in range(width):
            # get pixel at point (x,y)
            R,G,B = img_PIL.getpixel((x, y))
            bl = min(R,min(G,B))
            # set pixel to 4 empty img
            C.putpixel((x,y), (B,G,0))        
            M.putpixel((x,y), (B,0,R))          
            Y.putpixel((x,y), (0,G,R))
            K.putpixel((x,y),(bl,bl,bl))
    cyan =np.array(C)
    magenta= np.array(M)
    yellow= np.array(Y)
    black= np.array(K)

    CMYK.append(cyan)
    CMYK.append(magenta)
    CMYK.append(yellow)
    CMYK.append(black)

    return CMYK

img =img_PIL

color=Cvt2CMYK(img)
           #convert image to array (show image by opencv)

# show image
cv2.imshow("HINH GOC", original_img)
cv2.imshow("Kenh Mau Cyan", color[0])
cv2.imshow("Kenh Mau Magenta", color[1])
cv2.imshow("Kenh Mau Yellow", color[2])
cv2.imshow("Kenh Mau Black", color[3])

cv2.waitKey(0)
cv2.destroyAllWindows()