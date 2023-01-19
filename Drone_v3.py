
from djitellopy import Tello
import numpy as np
import cv2
import time, os, pickle
import threading
''' Python program to Scan and Read a QR code'''
from pyzbar.pyzbar import decode
#import cv2.aruco as aruco
'''Para realizar o Json'''
import requests
import json




class Tello_2:

    def __init__(self):
        #global cap
        self._running = True
        time.sleep(1)
        #self.video = cv2.VideoCapture("udp://192.168.10.1:11111")
        self.video = cv2.VideoCapture("udp://@0.0.0.0:11111")
        time.sleep(1)
        #self.video = cv2.VideoCapture(0)  # webcam

        #self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        #self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(3,640)
        self.video.set(4,480)


    def terminate(self):
        self._running = False
        self.video.release()
        cv2.destroyAllWindows()
        me.streamoff()
        #me.end()
        

    def infos(self):
        i = 0
        with open('parametros.txt') as f:
            MydataList = f.read().splitlines()

        time.sleep(1)
        while self._running:
            global frame, key, ret
            
            ret, frame = self.video.read()
            #frame = frame[0:360, 300:660]
            #frame = frame[0:660, 300:860]

            qrcode = decode(frame)

            for barcode in qrcode:
                #print(barcode.data)
                myData = barcode.data.decode('utf-8')
                print(myData)

                if myData in MydataList:
                    myoutput = 'Autorizado'
                    mycolor = (0,255,0)

                else:
                    myoutput = 'Não Autorizado'
                    mycolor = (0,0,255)

                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                #cv2.polylines(img,[pts],True,(176,196,222),3)
                cv2.polylines(frame,[pts],True,(mycolor),3)

                pts2 = barcode.rect
                #cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
                #cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,0.5,(176,196,222),1, cv2.LINE_AA)
                cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,0.5,(mycolor),1, cv2.LINE_AA)
                    
            try:
                

                if ret:
                    # Draw black background for textq
                    font = cv2.FONT_HERSHEY_PLAIN
                    #cv2.rectangle(frame, (0, 600), (0, 120), (255, 255, 255), -1)

                    #print bateria
                    energyT = me.get_battery()

                    if (i == 0):
                        energy = energyT
                        bat = str(energy)
                        cv2.putText(frame, str("Batery: " + bat), (20, 40), font, 1, (176,196,222), 2, cv2.LINE_AA)
                        i += 1

                    elif ((i>0) and (energyT == energy)):
                        bat = str(energy)
                        cv2.putText(frame, str("Batery: " + bat), (20, 40), font, 1, (176,196,222), 2, cv2.LINE_AA)
                        i = 0
                    
                    else:
                        i=0

                    cv2.imshow('Camera Online do Drone', frame)
                    
                    cv2.waitKey(1)
                
                    # Qr_Code
                
                key = cv2.waitKey(1) & 0xFF
                if key == 27:    #Apertar Esc para sair
                     
                    #self.video.release()
                    #cv2.destroyAllWindows()
                    recvThread2 = t.terminate()
                    recvThread2.start()
                    break


            except Exception as err:
                print(err)


'''INICIA DRONE'''

#Inicia drone em modo command e liga câmera
me = Tello()
me.connect()
time.sleep(1)
me.streamon()
#inicia thread de leitura da câmera

t = Tello_2()
recvThread = threading.Thread(target=t.infos)
recvThread.start()


# Main loop
#while True:
    # use 'q' to quit
    #me.end()