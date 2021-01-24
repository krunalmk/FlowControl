#server sends message

import socket
import time
import ctypes

isPrintAvl = True

def manualPrint(string):
    global isPrintAvl
    while not isPrintAvl:
        pass
    isPrintAvl = False
    print(string)
    isPrintAvl = True

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()
port = 9998
serversocket.bind((host, port))
serversocket.listen(5)
receivedMsg = ""
flag_for_threading_sent = 0
threadRunning = False

clientsocket,addr = serversocket.accept()      
print("Got a connection from %s" % str(addr))
print("Sent: Thank you for connecting")
msg = 'Thank you for connecting'+ "\r\n"

def sendAgain(message):
    receivedMsg = ""
    msg = ""
    global flag_for_threading_sent
    global threadRunning
    while msg.upper() != "EXIT":
        ind = 0
        flagACK0 = False
        msg = input("Enter msg: ")
        if msg.upper() == "EXIT":
            pass
        else:
            while ind < len(msg):
                flagACK0 = False
                x = 0
                message = msg[ind:ind+4]
                if message.upper() != "EXIT":
                    i=0
                    manualPrint("Sending frame now (data ="+ message+")")
                    clientsocket.send(message.encode())
                    for x in range (0, len(message)):
                        try:
                            clientsocket.settimeout(3)
                            receivedMsg = clientsocket.recv(4).decode()
                            manualPrint("Client sent:" + receivedMsg)
                        except socket.timeout:
                            manualPrint("Not received within 3 seconds")
                            manualPrint("So sending data again")
                            flagACK0 = True
                            ind += x
                            break
                        if receivedMsg == "ACK1":
                            flag_for_threading_sent = 0
                        else:
                            manualPrint("So sending again")
                            ind += x
                            flagACK0 = True
                            flag_for_threading_sent = 0
                            break
                if flagACK0 == False:
                    ind += 4
    else:
        clientsocket.send("exit".encode('ascii'))
        clientsocket.close()


while msg.upper() != "EXIT" and receivedMsg.upper() != "EXIT":
    sendAgain(msg)
else:
    clientsocket.send("exit".encode('ascii'))
    clientsocket.close()
