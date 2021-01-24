#server sends message

import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)                                           

receivedMsg = ""

clientsocket,addr = serversocket.accept()      
print("Got a connection from %s" % str(addr))
msg = 'Thank you for connecting'+ "\r\n"

def sendAgain(msg):
    receivedMsg = ""
    while msg.upper() != "EXIT":# and receivedMsg.upper() != "EXIT":
        clientsocket.send(msg.encode('ascii'))
        startTime = time.time()
        receivedMsg = clientsocket.recv(1024).decode('ascii')
        endTime = time.time()
        print("Client sent:", receivedMsg)
        if receivedMsg == "ACK1":
            print("Msg received in", endTime-startTime)
            msg = input("\nEnter msg: ")
            sendAgain(msg)
            return
        else:
            print("So sending again")
            sendAgain(msg)
            return
    else:
        clientsocket.close()

while msg.upper() != "EXIT" and receivedMsg.upper() != "EXIT":
    sendAgain(msg)
else:
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
