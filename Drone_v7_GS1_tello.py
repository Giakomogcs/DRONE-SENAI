
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
        self.video = cv2.VideoCapture("udp://@0.0.0.0:11111") #tello
        #self.video = cv2.VideoCapture("rtmp:10.84.30.32:1935/")



        ##self.video = cv2.VideoCapture("rtmp:10.84.22.194:1935/")
        #self.video = cv2.VideoCapture(0)  # webcam
        
        #self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        #self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(3,640)
        self.video.set(4,480)


    def terminate(self):
        global i,ids,past

        self._running = False
        self.video.release()
        cv2.destroyAllWindows()
        me.streamoff()
        i = 0
        ids = []
        past = []
        #me.end()


    def infos(self):
        global frame, key, ids, past, rload
        i = 0
        pd = False
        lc = False
        rload = False
        ids = []
        past = []

        while self._running:
            
            #time.sleep(0.2)
            try:
                ret, frame = self.video.read()
                #frame = frame[0:400, 200:660]
                #frame = frame[200:1300, 500:1400]

                if ret:

                    for barcode in decode(frame):
                        #print(barcode.data)
                        myData = barcode.data.decode('utf-8')
                        #myData = barcode.data.decode()

                        if myData in MydataList:
                            mycolor = (0,255,0) 

                            if ((myData not in past) and (len(ids) < 2)):

                                if ((myData not in ids) and (len(ids) < 2)):

                                    if ((myData in MydataListg) and (pd == False) and (len(ids) < 1)):
                                        ids.append(myData) #produto
                                        past.extend(ids) #protutos passados
                                        
                                        print('past:')
                                        print (past)
                                        print('ids:')
                                        print (ids)

                                        pd = True
                                        
                                    elif ((myData in MydataListh) and (lc == False) and (len(ids) == 1)):
                                        ids.append(myData) #local
                                        past.extend(ids) #protutos passados
                                        
                                        print('past:')
                                        print (past)
                                        print('ids:')
                                        print (ids)

                                        lc = True
                                     

                            if len(ids) == 2:
                                #past.extend(ids) #protutos passados
                                
                                print("POST")
                                post_msg()
                                

                                print(rload)
                                if rload == True:
                                    print(ids)  
                                    print(rload)    
                                    ids = []
                                    pd = False 
                                    lc = False
                                    rload = False  

                                    print('past:')
                                    print (past)
                                    print('ids:')
                                    print (ids)
                                              

                        else:
                            myoutput = 'Não Autorizado'
                            mycolor = (0,0,255)
                          

                        pts = np.array([barcode.polygon],np.int32)
                        pts = pts.reshape((-1,1,2))
                        #cv2.polylines(img,[pts],True,(176,196,222),3)
                        cv2.polylines(frame,[pts],True,(mycolor),5)

                        pts2 = barcode.rect
                        #cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
                        #cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,0.5,(176,196,222),1, cv2.LINE_AA)
                        cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,1,(mycolor),2, cv2.LINE_AA)

                    # Draw black background for textq
                    font = cv2.FONT_HERSHEY_PLAIN
                    cv2.rectangle(frame, (0, 600), (0, 120), (255, 255, 255), -1)
                    '''
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
                    '''

                    cv2.imshow('Camera Online do Drone', frame)
                    cv2.waitKey(1)
                
                   
                key = cv2.waitKey(1) & 0xFF
                if key == 27:    #Apertar Esc para sair
                     
                    #self.video.release()
                    #cv2.destroyAllWindows()

                    recvThread3 = threading.Thread(target=t.terminate)
                    recvThread3.start()
                    break


            except Exception as err:
                print(err)


def post_msg():
    print('entrei')
    global ids,rload

    #url = "http://10.1.1.231:3003/estoque"
    url = "http://localhost:3333/estoque"
    #url = "http://192.168.10.2:3333/estoque"
    #msgcode = str(msgcode)
    if ids[0] in MydataListg:
        prod = ids[0]
        #distri = ids[1].split('_')
        #loc = distri[0]
        #prat = distri[1]

        loc = ids[1]
        prat = "12"
    
    elif ids[0] in MydataListh:  
        prod = ids[1]
        #distri = ids[0].split('_')
        #loc = distri[0]
        #prat = distri[1]

        loc = ids[0]
        prat = "12"


    print("prod = "+prod)
    print("loc = "+loc)
    print("prat = "+prat)

    payload = json.dumps({
        "code": str(prod),
        "quantity": "1",
        #"shelf": "Prateleira OpenLab",
        "shelf": prat,
        "local": str(loc)
    })
    print("-----payload------")
    print(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    
    
    ids = []
    rload = True
        



def voo():
    
    #me.takeoff()
    #time.sleep(13)
    #me.land()
    
    me.takeoff()
    me.move_forward(200)
    time.sleep(1)
    me.move_down(35)
    time.sleep(1)
    me.move_forward(115)
    time.sleep(1)
    me.move_down(35)
    time.sleep(1)
    me.rotate_clockwise(90)
    time.sleep(1)
    #me.move_left(20)
    #time.sleep(1)
    me.move_forward(175)
    time.sleep(1)
    me.rotate_clockwise(90)
    time.sleep(1)
    me.move_left(40)
    time.sleep(1)
    me.move_left(40)
    time.sleep(1)
    me.move_left(40)
    time.sleep(1)
    #me.move_forward(30)
    #time.sleep(1
    me.move_down(72)
    time.sleep(1)
    me.move_right(40)
    time.sleep(1)
    me.move_right(40)
    time.sleep(1)
    me.move_right(40)
    time.sleep(1)
    me.rotate_clockwise(90)
    time.sleep(1)
    #me.move_right(40)
    time.sleep(1)
    me.move_up(100)
    time.sleep(1)
    me.move_forward(180)
    time.sleep(1)

    me.land()
    

'''INICIA DRONE'''

#Inicia drone em modo command e liga câmera
me = Tello()
me.connect()
time.sleep(1)
me.streamon()

with open('parametros.txt') as f:
    MydataList = f.read().splitlines()

with open('Produtos.txt') as g:
    MydataListg = g.read().splitlines()

with open('Locais.txt') as h:
    MydataListh = h.read().splitlines()


#inicia thread de leitura da câmera
t = Tello_2()
recvThread = threading.Thread(target=t.infos)
recvThread.start()

#voo()  

# Main loop
