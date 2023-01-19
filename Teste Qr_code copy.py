'''
import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('./teste qrcode/barcode21222.jpeg')

for barcode in decode(img):
    mydata = barcode.data.decode('utf-8')
    print(mydata)

'''
'''
import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('Qrcode_211201_0.png')
cap = cv2.VideoCapture(0)
print("Mandei gravar")
cap.set(3,1720)
cap.set(4,720)

while True:

    success,img = cap.read()
 
    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for barcode in decode(img):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)

    '''

'''
#preto e branco

import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('Qrcode_211201_0.png')
cap = cv2.VideoCapture(0)
print("Mandei gravar")
cap.set(3,1720)
cap.set(4,720)

while True:

    success,img = cap.read()
 
    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('video gray', grayFrame)


    for barcode in decode(grayFrame):
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

    
    #deu mais que o normal
'''   
'''
import numpy as np
import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,1720)
cap.set(4,720)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    contrast = 1.3
    brightness = 0.3
    frame[:,:,2] = np.clip(contrast * frame[:,:,2] + brightness, 0, 255)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    for barcode in decode(frame):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        #pts = np.array([barcode.polygon],np.int32)
        #pts = pts.reshape((-1,1,2))
        #cv2.polylines(img,[pts],True,(255,0,255),5)
        #pts2 = barcode.rect
        #cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

'''

import numpy as np
import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,680)
cap.set(4,420)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    contrast = 0.6
    brightness = 0.4
    frame2[:,:,2] = np.clip(contrast * frame2[:,:,2] + brightness, 2, 200)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_HSV2BGR)
    grayFrame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video gray', grayFrame)
    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    for barcode in decode(grayFrame):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(grayFrame,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(grayFrame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
