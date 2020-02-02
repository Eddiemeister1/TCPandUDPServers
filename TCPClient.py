#TCPClient.py
#Assignment #4
#By Eduardo Dotel
from socket import socket, AF_INET, SOCK_STREAM
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence: ')
clientSocket.send(message.encode('utf-8'))
modifiedMessage = clientSocket.recv(2048)
print('From Server: ', modifiedMessage)
clientSocket.close()