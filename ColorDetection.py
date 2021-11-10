import cv2
import numpy as np

# 0 == Bilgisayarda tanımlı ilk kamera
# 1 == usb
cap = cv2.VideoCapture(0)                                        # Kameradan alınan görüntüyü cap adındaki değişkene atıyor.

def nothing(x):
    pass

#Trackbar oluşturuluyor.
cv2.namedWindow("frame")
cv2.createTrackbar("H1", "frame", 0, 359, nothing)               # trackbarNAme, windowName, value(alt limit), count(üst limit), onChange(değişim)
cv2.createTrackbar("H2", "frame", 0, 359, nothing)     
cv2.createTrackbar("S1", "frame", 0, 255, nothing)
cv2.createTrackbar("S2", "frame", 0, 255, nothing)
cv2.createTrackbar("V1", "frame", 0, 255, nothing)
cv2.createTrackbar("V2", "frame", 0, 255, nothing)

while True:
    _, frame = cap.read()                                        # Okunan görüntü frame adındaki değişkene atanıyor. Virgülden öncesi kontrol amaçlı konulur.
    #frame = cv2.flip(frame, 1)
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)            # frame değişkeninden alınan görüntü HSV'ye dönüştürülüp hsvFrame adındaki değişkene atanıyor.

    H1 = cv2.getTrackbarPos("H1", "frame")                       # trackbarName, windowName
    H2 = cv2.getTrackbarPos("H2", "frame")                  
    S1 = cv2.getTrackbarPos("S1", "frame")
    S2 = cv2.getTrackbarPos("S2", "frame")
    V1 = cv2.getTrackbarPos("V1", "frame")
    V2 = cv2.getTrackbarPos("V2", "frame")


    # Renk değerlerini tutmak için lower ve upper adında 2 adet dizi oluşturup içerisine trackbardan alınan değerleri atıyoruz.
    lower = np.array([H1, S1, V1])
    upper = np.array([H2, S2, V2])
    
    # Maskeleme işlemi yapılıyor.
    mask = cv2.inRange(hsvFrame, lower, upper)                   # Görüntü, alt değer, üst değer

    # Maskeleme işlemi yapılıyor fakat bunda ekrandaki görüntü tespit edilen renk oluyor.
    res = cv2.bitwise_and(frame, frame, mask = mask)             # Alınan görüntü, atanan görüntü, maske
    
    # Görüntüleri ekranda gösteren fonksiyon
    cv2.imshow("frame", frame)                                   # windowName, gösterilecek görüntü
    cv2.imshow("res", res)
    cv2.imshow("mask", mask)

    # "q" harfine bastığımızda uygulamayı kapatmamızı sağlayan koşul bloğu
    if cv2.waitKey(1) &0XFF == ord("q"):                        
        break
cv2.destroyAllWindows()
