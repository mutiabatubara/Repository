import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    #membaca frame per frame
    ret, frame = cap.read()

    #merubah menjadi abu abu
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # menampilkan hasil frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#tutup aplikasi
cap.release()
cv2.destroyAllWindows()
