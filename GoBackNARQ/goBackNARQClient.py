#client sends ACK

import socket
import time

isPrintAvl = True

def meraPrint(string):
    global isPrintAvl
    while not isPrintAvl:
        pass
    isPrintAvl = False
    print(string)
    isPrintAvl = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9998
s.connect((host, port))                               

receivedMsg = ""
enterMsg = ""

reply = [ "ACK1", "ACK1", "ACK1", "ACK0", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1"]
k=0

while receivedMsg.upper() != "EXIT":
    receivedMsg = s.recv(4)
    if receivedMsg.upper() == "EXIT":
        pass
    else:
        for x in range(len(receivedMsg)):
            meraPrint ("Server sent: "+ chr(receivedMsg[x]))
            enterMsg = reply[k-1]
            if enterMsg == "ACK0":
                meraPrint("Sending "+ enterMsg)
                s.send(enterMsg.encode())
                for y in range (x, len(receivedMsg)):
                    meraPrint("Discarding "+ chr(receivedMsg[y]))
                k+=1
                break
            else:
                if receivedMsg.upper() != "EXIT":
                    #if k == 2:
                        #time.sleep(3.2)
                        #s.send(enterMsg.encode('ascii'))
                        #k+=1
                        #meraPrint("Sending 3.2s late")
                        #break
                    meraPrint("Sending "+ enterMsg)
                    meraPrint("")
                    s.send(enterMsg.encode('ascii'))
                else:
                    s.close()
                k+=1
else:
    s.close()
