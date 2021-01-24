#client sends ACK

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host, port))                               

receivedMsg = ""
enterMsg = ""

reply = ["ACK1", "ACK0", "ACK1", "ACK1", "ACK0", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1", "ACK1"]
k=0

while receivedMsg.upper() != "EXIT":
    receivedMsg = s.recv(1024)
    print ("Server sent:", receivedMsg.decode('ascii'))
    enterMsg = reply[k]
    print("Sending", enterMsg)
    print()
    if receivedMsg.upper() != "EXIT":
        s.send(enterMsg.encode('ascii'))
    else:
        s.close()
    k+=1
else:
    s.close()
