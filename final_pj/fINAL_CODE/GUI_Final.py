# Import thu vien
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from Function import funtion_login, GetImage, Complimentary, ExitWindow

window = tk.Tk()
window.title("Final Report")
colorBackground = "white"  
# window.geometry('1100x1000')
window.attributes('-fullscreen', True)
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

# Load hình ảnh
imgCKM = Image.open("fINAL_CODE\image\Khoa CKM.png").resize((850, 130), Image.ANTIALIAS)
imgShowCKM = ImageTk.PhotoImage(imgCKM)
img1 = Image.open("fINAL_CODE\image\Khoa.jpg").resize((224, 224), Image.ANTIALIAS)
imgShowKhoa = ImageTk.PhotoImage(img1)
img2 = Image.open("fINAL_CODE\image\Hà.jpg").resize((224, 224), Image.ANTIALIAS)
imgShowHa = ImageTk.PhotoImage(img2)
img3 = Image.open("fINAL_CODE\image\Hoài.jpg").resize((224, 224), Image.ANTIALIAS)
imgShowHoai = ImageTk.PhotoImage(img3)
img4 = Image.open("fINAL_CODE\image\Teacher.png").resize((224, 256), Image.ANTIALIAS)
imgShowTeacher = ImageTk.PhotoImage(img4)

login = tk.Frame(window)
frame1 = tk.Frame(window)


label_disease = tk.Label(frame1)
label_thresh = tk.Label(frame1)

frame1.grid(row = 0, column = 0, sticky = 'nsew')
login.grid(row = 0, column = 0, sticky = 'nsew')

Label(login, text = "UserName").place(x = 400, y = 640)
Label(login, text = "PassWord").place(x = 400, y = 675)

entry1 = Entry(login, bd = 7)
entry1.place(x = 470, y = 640)
entry2 = Entry(login, bd = 7, show = "*")
entry2.place(x = 470, y = 675)
login.tkraise()

login_programe = funtion_login(entry_1 = entry1, entry_2 = entry2, previous_frame = login, frame_name = frame1, label_name = label_disease,thresh = label_thresh)
get_img = GetImage(frame_name = frame1, label_name = label_disease, thresh = label_thresh)
comp = Complimentary(frame_name = frame1,  label_name = label_disease, thresh  = label_thresh)
 
#============================================= Frame Code =============================================#

#============================================= Frame Login =============================================#

# Load image 
login_img_1 = tk.Label(login, text="", image = imgShowCKM)
login_img_1.place(x=250, y=20)
login_img_2 = tk.Label(login, text="", image = imgShowKhoa)
login_img_2.place(x=400, y=330)
login_img_3 = tk.Label(login, text = "", image = imgShowHa)
login_img_3.place(x = 624, y = 330)
login_img_4 = tk.Label(login, text = "", image = imgShowHoai)
login_img_4.place(x = 848, y = 330)
login_img_5 = tk.Label(login, text = "", image = imgShowTeacher)
login_img_5.place(x = 80, y = 300)

# Create Text Label
lblNameID01 = tk.Label(login, text=" Ngành: Công nghệ kỹ thuật cơ điện tử", font = ('Arial', 20, 'bold'), fg = "#000080")
lblNameID01.place(x = 320, y = 170)
lblNameID04 = tk.Label(login, text="Đề Tài:  Phân đoạn và nhận dạng tổn thương trên da", font = ("Arial", 22, "bold"), fg = "#000080")
lblNameID04.place(x = 200, y = 220)

lblNameID05 = tk.Label(login, text="GVHD:", font = ("Arial", 14, "bold"), fg = "black")
lblNameID05.place(x = 150, y = 560)
lblNameID06 = tk.Label(login, text="Ts. Nguyễn Văn Thái", font = ("Arial", 14, "bold"), fg = "black")
lblNameID06.place(x = 85, y = 590)

lblNameID07 = tk.Label(login, text = "Sinh viên thực hiện: ", font = ("Arial", 16, "bold"), fg = "black")
lblNameID07.place(x = 400, y = 280)

lblNameID08 = tk.Label(login, text="Lê Đăng Khoa", font = ("Arial", 12 , "bold"), fg = "black")
lblNameID08.place(x = 450, y = 560)
lblNameID09 = tk.Label(login, text="MSSV: 20146497", font = ("Arial", 12 , "bold"), fg = "black")
lblNameID09.place(x = 440, y = 590)

lblNameID10 = tk.Label(login, text="Nguyễn Việt Hà", font = ("Arial", 12, "bold"), fg = "black")
lblNameID10.place(x = 670, y = 560)
lblNameID11 = tk.Label(login, text="MSSV: 20146489", font = ("Arial", 12 , "bold"), fg = "black")
lblNameID11.place(x = 670, y = 590)

lblNameID12 = tk.Label(login, text = "Đỗ Sĩ Hoài", font = ("Arial", 12, "bold"), fg = "black")
lblNameID12.place(x = 920, y = 560)
lblNameID13 = tk.Label(login, text="MSSV: 20146491", font = ("Arial", 12 , "bold"), fg = "black")
lblNameID13.place(x = 900, y = 590)

Button(login, text = "Login", height = 1 , width = 12, bd = 9, command = login_programe.loginx, bg = "blue", font = ('Arial', 11, 'bold')).place(x = 470, y = 720)
#=============================================End Frame Login =============================================#

#============================================= Frame 1 ====================================================#
# # Create Text Label
lblNameID1 = tk.Label(frame1, text = "Đề tài: Phân đoạn và nhận dạng tổn thương trên da ", font = ('Arial', 24, 'bold'), fg = "#000080")
lblNameID1.place(x = 180, y = 10)

#=================================================================================================================#
#============================================= Create Button  ====================================================#

btn_brower = tk.Button(frame1, text = "Browse Image", height = 2, width = 15, bd = 9, command = get_img.Browse_Image, bg = "green",
                       font=('Arial', 11, 'bold'))
btn_brower.place(x = 10, y = 100)

btn_predict = tk.Button(frame1, text = "Detect Disease", height = 2, width = 15, bd = 9, command = comp.Disease_Predict, bg = "green",
                       font = ('Arial', 11, 'bold'))
btn_predict.place(x = 10, y = 170)

btn_segmentation = tk.Button(frame1, text = "View Segment", height = 2, width = 15, bd = 9, command = comp.run_segmentation, bg = "green",
                       font = ('Arial', 11, 'bold'))
btn_segmentation.place(x = 10, y = 240)

btn_detect = tk.Button(frame1, text = "View Contour", height = 2, width = 15, bd = 9, command = comp.detect, bg = "green",
                        font = ('Arial', 11, 'bold'))
btn_detect.place(x = 10, y = 310)

btn_HSV = tk.Button(frame1, text = "View HSV ", height = 2, width = 15, bd = 9, command = comp.run_HSV, bg = "green",
                       font = ('Arial', 11, 'bold'))
btn_HSV.place(x = 10, y = 380)

btn_segmentation = tk.Button(frame1, text = "View Histogram", height = 2, width = 15, bd = 9,command = comp.view_histogram, bg = "green",
                       font = ('Arial', 11, 'bold')) 
btn_segmentation.place(x = 10, y = 450)

frame1_BackBtn = tk.Button(frame1, text = "Back", height = 2,width = 15,bd = 9, command = login_programe.go_back, bg = "red",
                        font = ('Arial', 11, 'bold'))
frame1_BackBtn.place(x = 10, y = 550)

frame1_exitBtn = tk.Button(frame1, text = "Exit", height = 2, width = 15,bd = 9, command = ExitWindow(window).confirm_exit, bg = "red",
                        font = ('Arial', 11, 'bold'))
frame1_exitBtn.place(x = 10, y = 620)

#======================================================End Create Button==========================================#

#=========================================================INFORMATION=============================================#

name_disease = tk.Label(frame1, text="Disease Predict: ", font=('Arial', 15, 'bold'), fg="black")
name_disease.place(x=10, y=700)

Threshold = tk.Label(frame1, text="Threshold: ", font=('Arial', 15, 'bold'), fg="black")
Threshold.place(x=420, y=700)

img_ori = tk.Label(frame1, text="Original Image", font=('Arial', 15, 'bold'),fg="black")
img_ori.place(x=370, y=100)

img_seg = tk.Label(frame1, text="Segmentation Image", font=('Arial', 15, 'bold'),fg="black")
img_seg.place(x=350, y=390)

img_detect = tk.Label(frame1, text="Injured Area", font=('Arial', 15, 'bold'),fg="black")
img_detect.place(x=850, y=390)

img_detect = tk.Label(frame1, text="HSV Image", font=('Arial', 15, 'bold'),fg="black")
img_detect.place(x=850, y=100)
#===========================================================END===================================================#

window.mainloop()