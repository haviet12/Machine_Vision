
import cv2
import numpy as np

def otsu(img):
    hist = cv2.calcHist([img],[0],None,[256],[0,255]) # tính histogram của ảnh

    hist_norm = hist.ravel()
    phuong_sai_t = 0 
    M,N = img.shape
 

    for nguong in range(256):
        Tong_gt_xam_A = 0  
        Tong_gt_xam_B = 0  
        Tong_pixel_A = 0  
        Tong_pixel_B = 1   
     

        for x in range (0,256):
            if x >= nguong:
               Tong_pixel_A += hist_norm[x]
               Tong_gt_xam_A += x*(hist_norm[x]/M*N)
            else:
                Tong_pixel_B += hist_norm[x]
                Tong_gt_xam_B += x*(hist_norm[x]/M*N)
        
        mG = Tong_gt_xam_A + Tong_gt_xam_B  # cuong do trung binh cua anh

        P1 =Tong_pixel_A/(M*N)  # tong xac suat tich luy
        P2 =Tong_pixel_B/(M*N)

        m1 = Tong_gt_xam_A/P1   # gtri cuong do trung binh cua pixel
        m2 = Tong_gt_xam_B/P2     
        phuong_sai = P1*((m1-mG)**2)+P2*((m2-mG)**2) 
       


        if (phuong_sai > phuong_sai_t):
            phuong_sai_t = phuong_sai
            nguong_toi_uu = nguong  



    print("Ngưỡng tìm được", nguong_toi_uu)
    return nguong_toi_uu



def phan_doan_bang_cat_nguong(img, nguong):
    img_phan_doan = np.zeros_like(img)
    m, n = img.shape
    for i in range(m):
        for j in range(n):
            if (img[i,j] < nguong):
                img_phan_doan[i,j] = 0
            else:
                img_phan_doan[i,j] = 225 
    return img_phan_doan
