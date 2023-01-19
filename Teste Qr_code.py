import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('Qrcode_211201_0.png')
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("rtmp:192.168.0.16:1935/")
print("Mandei gravar")
cap.set(3,1700)
cap.set(4,700)

while True:

    success,img = cap.read()

    for barcode in decode(img):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        #pts = np.array([barcode.polygon],np.int32)
        #pts = pts.reshape((-1,1,2))
        #cv2.polylines(img,[pts],True,(255,0,255),5)
        #pts2 = barcode.rect
        #cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)