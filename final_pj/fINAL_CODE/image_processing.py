import cv2
import numpy as np
import os
# from utils import read_resize
import splitfolders as sp
from PIL import Image
from matplotlib import pyplot as plt

from math import *




def histogram_equalization_rgb(image):
    # convert RGB => YUV
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_yuv[0,:,:] = cv2.equalizeHist(img_yuv[0,:,:])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return img_output


def resize_and_save_images(input_folder, output_folder, new_width, new_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of images in the input folder
    folder_list = os.listdir(input_folder)

    for folder in folder_list:
        folder_name_input=os.path.join(input_folder, folder)

        folder_name_output=os.path.join(output_folder, folder)
        if not os.path.exists(folder_name_output):
            os.makedirs(folder_name_output)

        image_list = os.listdir(folder_name_input)
        # print(image_list)
        for image_name in image_list:
            # Construct the input and output file paths
            # input_path = os.path.join(input_folder,folder,image_name)
            input_path = os.path.join(input_folder, folder, image_name.replace('\\', '\\\\'))


            image = cv2.imread(input_path)
            resized_image = cv2.resize(image, (new_width, new_height))
            

            output_path = os.path.join(output_folder, folder, image_name.replace('\\', '\\\\'))
            cv2.imwrite(output_path, resized_image)
            


# resize data to the same size

original_folder='dataset'
output_folder_resize='datasets_resize'
new_width=224
new_height=224

resize_and_save_images(original_folder, output_folder_resize, new_width, new_height)
####################################################################################
# input_folder = "datasets_resize"
# folder_list = os.listdir(input_folder)
# # print(folder_list)
# # list=[]
# for folder in folder_list:
#     folder_path= os.path.join(input_folder,folder)

#     image_name = os.listdir(folder_path)
#     for img in image_name:
#         image_path=os.path.join(folder_path,img.replace('\\', '\\\\'))
#         image = cv2.imread(image_path)
#         ## can bang histogram cho anh 
#         hist_img=histogram_equalization_rgb(image)
#         ## luu lai anh 
#         cv2.imwrite(image_path, hist_img)
    





#################################



# #### chia dữ liệu


# Đường dẫn tới thư mục chứa dữ liệu ảnh ban đầu
input_folder = "datasets_resize"
output_folder = "data"
# Đường dẫn tới thư mục đích để chứa các tập tin sau khi chia
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Tỷ lệ phần trăm cho các tập train, validation và test
train_ratio = 0.8
val_ratio = 0.1
test_ratio =0.1


# Thực hiện chia dữ liệu ảnh
sp.ratio(input_folder, output_folder, seed=42, ratio=(train_ratio, val_ratio, test_ratio))




