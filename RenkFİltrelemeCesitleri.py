import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
dusuk=np.array([90,30,30])#EN DÜŞÜK 90 AL EN YÜKSEK 130,EN DÜŞÜK 
yuksek=np.array([130,255,255])

while True:
    ret,kare=kamera.read()
    hsv=cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,dusuk,yuksek)
    son_resim=cv2.bitwise_and(kare,kare,mask=mask)
    
    
    #SMOOTHEED(YUMUSATMA)
    kernel=np.ones((15,15),dtype=np.float32)/225
    smoothed=cv2.filter2D(son_resim,-1,kernel)
    
    #BLURLAMA İŞLEMİ
    blur=cv2.GaussianBlur(son_resim,(15,15),0)
    
    #MEDYAN ÖZELLİĞİ
    
    medyan=cv2.medianBlur(son_resim,15)
    
    #BİLETERAL ÖZELLİĞİĞ
    bilateral=cv2.bilateralFilter(son_resim,15,75,75)
    cv2.imshow("video6",bilateral)
    cv2.imshow("Video5",medyan)
    cv2.imshow("Video4",son_resim)
    cv2.imshow("Video3",blur)
    cv2.imshow("video",kare)
    cv2.imshow("video2",smoothed)
    cv2.imshow("video7",hsv)
    
    
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
print(kernel)  
kamera.release()
cv2.destroyAllWindows()
        
