
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
import pandas as pd



class Tello_2:

    def __init__(self):
        self._running = True
        #self.video = cv2.VideoCapture("udp://192.168.10.1:11111")
        #self.video = cv2.VideoCapture("udp://@0.0.0.0:11111")
        #self.video = cv2.VideoCapture("rtmp:10.84.30.32:1935/")


        self.video = cv2.VideoCapture("rtmp:10.84.82.101:1935/")
        ##self.video = cv2.VideoCapture(0)  # webcam
        
        #self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        #self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(3,640)
        self.video.set(4,480)


    def terminate(self):
        global i,ids,past

        self._running = False
        self.video.release()
        cv2.destroyAllWindows()
        
        i = 0
        ids = []
        past = []
        


    def infos(self):
        global frame, key, ids, past, rload, cod, myData
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
                frame = frame[200:1300, 600:1300]

                if ret:

                    for barcode in decode(frame):
                        myData = barcode.data.decode('utf-8')
                        print(myData)

                        scan(myData) #vai zazer o scan
                        
                        #print(DataPL)

                        if myData != '' and (DataPL == 'Local' or DataPL == 'Produto'): #verifica se existe o codigo lido no excel
                            mycolor = (0,255,0) 
                            

                            if ((myData not in past) and (len(ids) < 2)):

                                if ((myData not in ids) and (len(ids) < 2)):

                                    if ((DataPL == 'Produto') and (pd == False) and (len(ids) < 1)):
                                        ids.append(myData) #produto
                                        past.extend(ids) #protutos passados

                                        print(ids)
                                        pd = True
                                        
                                    elif ((DataPL == 'Local') and (lc == False) and (len(ids) == 1)):
                                        ids.append(myData) #local
                                        past.extend(ids) #protutos passados

                                        print(ids)
                                        lc = True
                                     

                            if len(ids) == 2:
                                #past.extend(ids) #protutos passados
                                
                                post_msg()
                                print(ids) 

                                print(rload)
                                if rload == True:
                                    print(ids)  
                                    print(rload)    
                                    ids = []
                                    pd = False 
                                    lc = False
                                    rload = False     

                        else:
                            myoutput = 'Não Autorizado'
                            mycolor = (0,0,255)

                        if (DataPL ==''):
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
    
            
            
            
def scan(data): 
    global DataPL, loc, Dloc, prod
    DataPL = ''

    if myData.isdigit():
        dataMod = int(data)
        #print(type(dataMod))
    else:
        dataMod = str(data)
        #print(type(dataMod))

    try:
        try:
            filtroP = cod['Produto'] == dataMod #gera tabela true e false
            filtroPi = (cod[filtroP].iloc[0,2])
            #filtroBoolP = (filtroP[0] == True)  #saber se tem mesmo true
            DataPL = 'Produto'
            prod = data
            #print(filtroPi)

        except:
            filtroL = cod['Local'] == dataMod #gera tabela true e false
            filtroLi = (cod[filtroL].iloc[0,0])
            filtroLiDescri = (cod[filtroL].iloc[0,1])
            #filtroBoolL = (filtroL[0] == True)  #saber se tem mesmo true
            DataPL = 'Local'
            loc = data
            Dloc = filtroLiDescri
            #print(filtroLi)
    except:
        DataPL = ''
    
    #print(DataPL)
    return DataPL


def post_msg():
    print('entrei')
    global ids,rload

    #print(prod)
    #print(loc)
    #print(Dloc)

    #url = "http://10.1.1.231:3003/estoque"
    url = "http://localhost:3333/estoque"
    #url = "http://192.168.10.2:3333/estoque"
    #msgcode = str(msgcode)


    payload = json.dumps({
        "code": str(prod),
        "quantity": "1",
        #"shelf": "Prateleira OpenLab",
        "shelf": str(Dloc),
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

    
          

        

cod = pd.read_excel(r"C:\Drone\codigos_GS1_v2.xlsx", engine='openpyxl')

#inicia thread de leitura da câmera
t = Tello_2()
recvThread = threading.Thread(target=t.infos)
recvThread.start()

# Main loop
