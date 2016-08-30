from socket import *
import pickle
import re
def client(inputData):
    #server_address ="52.5.246.8"
    #SERVER ="127.0.0.1"
    SERVER ="172.31.141.117"
    PORT = 20000
    buffer_size = 32768
    ADD = (SERVER, PORT)
    tcpCliSock = socket(AF_INET,SOCK_STREAM) #based on socket stream
    tcpCliSock.connect(ADD)
    print "ready for inputs\n"
    print "Format of input: From address,To address,Time,Depart by or Arrive by,Date"
    print "Example: Claymont,Trenton,05:00PM,D,04/30/2015"
    # Filter inappropriate inputs
    print inputData
    pattern=re.compile(r'^\D+,\D+,(0[1-9]|1[012]):[0-5][0-9](AM|PM),[AD],(\d{2})[/.-](\d{2})[/.-](\d{4})$')
    match = pattern.match(inputData)
    if not match:
        dataReceived="User input is not in correct format."
    else:
        while True:
            # Then send the input to server
            print inputData
            tcpCliSock.send(inputData)
            # Read output from server
            dataReceived = tcpCliSock.recv(buffer_size)
            print dataReceived
            if dataReceived:
                break
        tcpCliSock.close()
    return dataReceived
#client("Hunting park station,City hall station,02:00PM,D,04/24/2015")

