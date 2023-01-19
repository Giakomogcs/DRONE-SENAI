
from djitellopy import Tello
import numpy as np
import cv2
import time, os, pickle
import threading
''' Python program to Scan and Read a QR code'''
from pyzbar.pyzbar import decode
'''Para realizar o Json'''
import requests
import json



class Tello_2:

    def __init__(self):
        self._running = True
        #self.video = cv2.VideoCapture("udp://192.168.10.1:11111")
        self.video = cv2.VideoCapture("udp://@0.0.0.0:11111")
        #self.video = cv2.VideoCapture(0)  # webcam
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


    def terminate(self):
        self._running = False
        self.video.release()
        cv2.destroyAllWindows()
        me.streamoff()
        #me.end()
        

    def infos(self):
        i = 0
        while self._running:
            try:
                global frame, key
                ret, frame = self.video.read()
                frame = frame[0:360, 300:660]
                
                if ret:
                    # Draw black background for textq
                    font = cv2.FONT_HERSHEY_PLAIN
                    cv2.rectangle(frame, (0, 600), (0, 120), (255, 255, 255), -1)

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

                    for barcode in decode(frame):
                        #print(barcode.data)
                        myData = barcode.data.decode('utf-8')
                        print(myData)
                        pts = np.array([barcode.polygon],np.int32)
                        pts = pts.reshape((-1,1,2))
                        cv2.polylines(frame,[pts],True,(255,0,255),5)
                        pts2 = barcode.rect
                        cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,0.9,(255,0,255),2, cv2.LINE_AA)
                
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