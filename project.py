#import socket module
from socket import *
from threading import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:], 'r')

        header = "HTTP/1.1 200 OK\r\nDate: Sun, 26 Sep 2014 20:09:20 GMT\r\nServer: localhost\r\n\r\n"
        outputdata = header + f.read()

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])

        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        header = "HTTP/1.1 404 Not Found\r\n\r\n"
        
        connectionSocket.send(header+"<html><body>404 Not Found</body></html>")
        connectionSocket.close()

    serverSocket.close()
