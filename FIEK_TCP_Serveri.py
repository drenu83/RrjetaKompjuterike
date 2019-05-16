
from socket import *
import datetime
import random
import threading
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print('--------------FIEK TCP Serveri----------------')
print('Serveri u startua ne localhost me portin:'+str(serverPort))
serverSocket.listen(5)
print('Serveri eshte i gatshem te pranoj kerkesa ')
print('----------------------------------------------')

def IPADRESA():
    return('IP Adresa e klientit te lidhur eshte: %s ' %address[0])


def NUMRIIPORTIT():
    return('Porti i klientit te lidhur eshte : %s' %address[1])

def BASHKETINGELLORE(clientWord):
    numratori=0
    lista=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Z']
    for i in str(clientWord):
        if i in lista:
            numratori+=1
    return str(numratori)
        
def PRINTIMI(word):
    words=str(word).strip()
    return words
    
def EMRIIKOMPJUTERIT():
    emriikompjuterit,pmt2,IPa=gethostbyaddr(address[0])
    if emriikompjuterit=="":
        print("Emri i kompjuterit nuk gindet! ")
    return str('Emri i kompjuterit eshte: ' + emriikompjuterit)
     
def KOHA():
    now = datetime.datetime.now()
    return ('Koha ne kete moment eshte: ' + now.strftime("%H:%M:%S"))

def LOJA():
    vargu = []
    for i in range(7):
        vargu.append(random.randint(1,49))
    vargu.sort()
    varguString=str(vargu)
    return('7 numrat e rastesishem jane:' + varguString)

def FIBONACCI(insertNumber):
    a = 1
    b = 0
    c = 0
    try:
        c = int(insertNumber)
    except:
        return "Ka nje gabim"
    if c<1:
        return "Ka nje gabim, numri duhet te jete me i madh se 1"
    for i in range(c-1):
        a = a + b
        b = a - b
    numri=str(a)
    return("Numri pasues ne serine Fibonacci eshte: " + numri)


def KONVERTIMI(zgjedhja, insertValue):
    vlera=float(insertValue)
    if zgjedhja=="KILOWATTTOHOURSEPOWER":
        vlera=vlera*1.3410220896
    elif zgjedhja=="HOURSEPOWERTOKILOWATT":
        vlera=vlera* 0.7456998716
    elif zgjedhja=="DEGREESTORADIANS":
        vlera=vlera*0.0174532925
    elif zgjedhja=="RADIANSTODEGREES":
        vlera=vlera*57.295779513
    elif zgjedhja=="GALLONSTOLITERS":
        vlera=vlera*3.78541178
    elif zgjedhja=="LITERSTOGALLONS":
        vlera=vlera*0.26
   
    else:
        print("Keni bere zgjedhjen gabim")
    vleraPerf=str(vlera)
    return (vleraPerf)
   
                                        
def FUQIA(n):
    number_n=int(n)
    p=2
    katrori=int(number_n)**p
    return katrori


def PRAPAFJALA(fjale):
    variable=fjale
    variable1=variable.lower()
    message = ""
    for b in variable1:
     message = b+message
    return message
    

def Klienti(connectionSocket, addr):
      
      try:
        while 1:  
          #ClientRecieve="Empty"
          print('Klienti u lidh ne serverin %s me port %s' % address)
          ClientRecieve = connectionSocket.recv(1024)
          ClientRecieveStr=str(ClientRecieve.decode().strip())
          ClientRecieveVarg=ClientRecieveStr.split(' ')  
          shtesa=ClientRecieveVarg[0]
          

          if ClientRecieveStr=="IPADRESA":
           connectionSocket.send(IPADRESA().encode())

          elif ClientRecieveStr=="NUMRIIPORTIT":
            connectionSocket.send(NUMRIIPORTIT().encode())

          elif ClientRecieveVarg[0]=="BASHKETINGELLORE":
            fjaliaedhene=ClientRecieveStr.replace(shtesa,"",1)
            numeruesi="Ne fjaline e dhene jane: " + BASHKETINGELLORE(fjaliaedhene.strip()) + " bashketingellore"
            connectionSocket.send(numeruesi.encode())

          elif ClientRecieveVarg[0]=="PRINTIMI":
            fjala=ClientRecieveStr.replace(shtesa,"",1)
            printo="Teksti i printuar eshte: " + PRINTIMI(fjala).strip()
            connectionSocket.send(printo.encode())

          elif ClientRecieveStr=="EMRIIKOMPJUTERIT":
           connectionSocket.send(EMRIIKOMPJUTERIT().encode())

          elif ClientRecieveStr=="KOHA":
            connectionSocket.send(KOHA().encode())

          elif ClientRecieveStr=="LOJA":
            connectionSocket.send(LOJA().encode())

          elif ClientRecieveVarg[0]=="FIBONACCI":
              givenNumber=ClientRecieveStr.replace(shtesa,"",1)
              print_printed=FIBONACCI(givenNumber).strip()
              connectionSocket.send(print_printed.encode())

          elif ClientRecieveVarg[0]=="FUQIA":
               numer=ClientRecieveStr.replace(shtesa,"",1)
               shfaq=str(FUQIA(numer)).strip()
               connectionSocket.send(shfaq.encode())

          elif ClientRecieveVarg[0]=="PRAPAFJALA":
            fjale1=ClientRecieveStr.replace(shtesa,"",1)
            printo="Fjala e kthyer prapa eshte: " + PRAPAFJALA(fjale1).strip()
            connectionSocket.send(printo.encode())

          elif ClientRecieveVarg[0]=="KONVERTIMI": #Varg[0]="KONVERTIMI", varg[1]=lloji i konvertimit, varg[2]=vlera per konvertim
              for i in range(len(ClientRecieveVarg)):
                    if "" in ClientRecieveVarg:
                        ClientRecieveVarg.remove("")
              convertedValue ="Vlera: " + ClientRecieveVarg[2] +  " eshte e barabarte me  " + KONVERTIMI(str(ClientRecieveVarg[1]).upper(),ClientRecieveVarg[2]) 
              connectionSocket.send(str(convertedValue).encode())
        

          else:
              print("Asnjera nga metodat")
              connectionSocket.close()
      except ValueError:
          print("Ka ndodhur nje gabim")
   
while 1:
     connectionSocket, address = serverSocket.accept();
     threading._start_new_thread(Klienti,(connectionSocket,address)) 

