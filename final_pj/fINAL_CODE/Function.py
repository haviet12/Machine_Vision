# Import thu vien
import cv2
import numpy as np
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import imutils
from tkinter import messagebox
from tkinter import filedialog 
from Segmentation_Otsu import otsu, phan_doan_bang_cat_nguong
from matplotlib import pyplot as plt
from keras.models import load_model

# Load model
model = load_model('fINAL_CODE\model_3.h5', compile = False)

previous_prediction = ""
present_path =""
count_login =0
img_phan_doan = np.zeros((224,224), dtype=np.uint8)
brower_image = 0

if present_path != "":
    img = Image.open(present_path)
    img_tk = ImageTk.PhotoImage(img)

    img_label_hsv=tk.Label(image= img_tk)
    img_label_segmented=tk.Label(image= img_tk)
    img_label_detect=tk.Label(image= img_tk)
    img_label = tk.Label(image= img_tk)
else : pass
#=================================================================================================================#
#==================================================== Class ======================================================#
class GetImage:
    def __init__(self,frame_name, label_name, thresh):
        self.frame_name = frame_name
        self.label_name = label_name
        self.thresh = thresh

    def Browse_Image(self):
        global img_label
        global brower_image  
        global present_path
        present_path = filedialog.askopenfilename(initialdir="test_images", title="Select Image", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))
        if present_path != None:
            # Display the selected image in the GUI
            img = Image.open(present_path).resize((224,224))
            img_tk = ImageTk.PhotoImage(img)
            # canvas.create_image(10,10, anchor=NW, image=img_tk)
            img_label = tk.Label( self.frame_name, image=img_tk)
            img_label.image = img_tk
            img_label.place(x=330, y=150)

            brower_image +=1
        if brower_image>=2:
            self.clear_data()

    def clear_data(self):
      
        img_label_segmented.config(image="")
        img_label_detect.config(image="")
        img_label_hsv.config(image="")
        self.label_name.config(text="")
        self.thresh.config(text="") 
   
class funtion_login(GetImage):
    
    def __init__(self,entry_1,entry_2,previous_frame,**kwargs):
        self.previous_frame = previous_frame
        self.entry1 =entry_1
        self.entry2 =entry_2
        super().__init__(**kwargs)
        
    def loginx(self):
        global count_login
        global img_label
        username = self.entry1.get()
        password = self.entry2.get()

        if username == '1' and password == '1':
            self.frame_name.tkraise()

            print('show success')
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')

            count_login +=1
            
            if count_login >=2 and present_path != None:
                ask = messagebox.askyesno("Confirmation", "Do you want to clear all result ? ")
                if ask :
                    self.clear_data()
                    img_label.config(image='')
                    print('#######################################################################################')
                else: 
                    pass

        else:
            messagebox.showerror("", "Sai tên tài khoản hoặc mật khẩu!")
    def go_back(self):
        self.previous_frame.tkraise()

class ExitWindow :
    def __init__(self,window):
        self.window = window
    
    def confirm_exit(self):
        result = messagebox.askyesno("Confirmation", "Are you sure you want to exit?")
        if result:
            self.window.quit()


class Complimentary(GetImage):
    def __init__(self, **kwargs):
      
        super().__init__(**kwargs)
    def run_segmentation(self):
        global img_phan_doan
        global img_label_segmented

        # reading image in gray scale
        img_seg = cv2.imread(present_path, 0)
        nguong= otsu(img_seg)

        img_phan_doan=phan_doan_bang_cat_nguong(img_seg,nguong)

        self.thresh.config(text= nguong, font=("Arial", 14, 'bold'),fg="#770000")
        self.thresh.place(x=550, y=700) 

        # Display the segmented image in the frame 2
        img_segmented = Image.fromarray(img_phan_doan)
        img_segmented = img_segmented.resize((224,224))  # Resize the image 
        img_segmented_tk = ImageTk.PhotoImage(img_segmented)
        img_label_segmented = tk.Label( self.frame_name, image=img_segmented_tk)
        img_label_segmented.image = img_segmented_tk        
        img_label_segmented.place(x=330, y=440)

    def run_HSV(self):
        global img_label_hsv
        # Display the HSV image in the Frame 2
        img_HSV = cv2.imread(present_path)
        img_hsv = cv2.cvtColor(img_HSV, cv2.COLOR_BGR2HSV)
        img_hsv_resized = cv2.resize(img_hsv, (224,224)) # Resize the image
        img_hsv_segmented = Image.fromarray(img_hsv_resized)
        img_hsv_tk = ImageTk.PhotoImage(img_hsv_segmented)
        img_label_hsv = tk.Label( self.frame_name, image=img_hsv_tk)
        img_label_hsv.image = img_hsv_tk  
        img_label_hsv.place(x=800, y=150)

    def Disease_Predict(self):
        global previous_prediction

        img = Image.open(present_path).resize((224,224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction using the loaded model
        prediction = model.predict(img_array)
        class_labels = ['Daysungtietba', 'not ruoi','ton thuong  mach mau','ung thu bieu mo','ung thu hac to']
        predicted_label = class_labels[np.argmax(prediction)]
        print(f'####################: {prediction}')
        previous_prediction = predicted_label
     
        self.label_name.config(text= predicted_label, font=("Arial", 15, 'bold'),fg="#770000")
        self.label_name.place(x=180, y=700)   
    
    def detect(self):
        global img_label_detect

        image = cv2.imread(present_path)
        img_gray_cv2 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        thresh = otsu(img_gray_cv2) 
        _, img_binary = cv2.threshold(img_gray_cv2, thresh,255, cv2.THRESH_BINARY_INV)
        contours = cv2.findContours(img_binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts =imutils.grab_contours(contours)
        img_result = image.copy()
        countContours = 0
        for cnt in cnts:
            c_area = cv2.contourArea(cnt)
            if c_area >=10000 and c_area <50176:
                countContours += 1
                cv2.drawContours(img_result,[cnt], -1, (0,255,0) , 2)
            if c_area < 10000 and c_area >400:
                countContours += 1
                cv2.drawContours(img_result,[cnt], -1, (0,255,0) , 2)

        # img_hsv_segmented = Image.fromarray(img_result)
        img_result = cv2.resize(img_result,(224,224))
        img_detect = Image.fromarray(img_result)
        img_detect_tk = ImageTk.PhotoImage(img_detect)
        img_label_detect = tk.Label( self.frame_name, image=img_detect_tk)
        img_label_detect.image = img_detect_tk  
        img_label_detect.place(x=800, y=440)

    def view_histogram(self):
        img_cv2 = cv2.imread(present_path)
        img_result = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
        # Vẽ và hiển thị ảnh gốc, histogram ảnh gốc và ảnh phân đoạn
        fig2 = plt.figure(figsize=(14, 8))  # Tạo vùng vẽ tỷ lệ 16:9
        # Tạo 4 vùng vẽ con
        (ax1, ax2), (ax3, ax4) = fig2.subplots(2, 2)
        ax1.imshow(img_result)
        ax1.set_title('Ảnh gốc')
        ax1.axis('off')

        # Hiển thị histogram ảnh gốc
        ax2.hist(img_result.flatten(), bins=256)
        ax2.set_title('Hitogram ảnh gốc')

        # Hiển thị ảnh phân đoạn
        ax3.imshow(img_phan_doan, cmap='gray')
        ax3.set_title('Ảnh phân đoạn dựa vào tìm ngưỡng Otsu')
        ax3.axis('off')

        # Hiển thị histogram ảnh phân đoạn
        ax4.hist(img_phan_doan.flatten(), bins=256)
        ax4.set_title('Hitogram ảnh phân đoạn')
        plt.show()

  