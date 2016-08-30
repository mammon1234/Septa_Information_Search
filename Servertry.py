import os
from time import sleep
from socket import *
import septa

Host=""
Port=20000
buffer_size=32768
Add=(Host,Port)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcpSerSock.bind(Add)
tcpSerSock.listen(5)

while True:
    print "Ready for connection"
    tcpCliSock,addr=tcpSerSock.accept()
    print "....connected from",addr
    while True:
        dataReceived=tcpCliSock.recv(buffer_size)
        if not dataReceived:
            break
        sleep(0.5)
        array=dataReceived.split(',')
        resultData=septa.septa(array[0],array[1],array[2],array[3],array[4])
        tcpCliSock.send(resultData)
        if resultData:
            break
        resultData=''
    tcpCliSock.close()
tcpSerSock.close()
    
