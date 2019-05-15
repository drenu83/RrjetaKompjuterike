import socket
import os
serverName = 'localhost'
serverPort = 12000
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect((serverName,serverPort))

def cls():
    os.system('cls')

while 1:
    
    try:
        print("------------------FIEK TCP Klienti--------------------")
        print("""
                Ju lutem shtypni njeren nga kerkesat:
                IPADRESA
                NUMRIIPORTIT   
                BASHKETINGELLORE   
                PRINTIMI
                EMRIIKOMPJUTERIT 
                KOHA
                LOJA   
                FIBONACCI 
                KONVERTIMI  -  KILOWATTTOHOURSEPOWER, HOURSEPOWERTOKILOWATT, DEGREESTORADIANS,
                               RADIANSTODEGREES, GALLONSTOLITERS, LITERSTOGALLONS
                FUQIA
                PRAPAFJALA
              """)
        print('------------------------------------------------------ ')
        ClientReq = input("Mesazh: Lidhja me server tani eshte kryer\n-------------------------------------------\n").upper()
        if ClientReq!='':
            ClientSocket.sendall(str.encode(ClientReq))
            data = ClientSocket.recv(128)
            print('-------------------------------------------')
            print(str(data.decode()))
            print('-------------------------------------------')
            print("Shtypni 'ENTER' per te vazhduar")
            input()
            cls()
               
    except ValueError:
        print("Ka ndodhur nje gabim")
        
ClientSocket.close()





