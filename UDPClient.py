#UDPClient.py
#Assignment #4
#By Eduardo Dotel
#The time portion of the code is credited to the answer for the question in:
#https://stackoverflow.com/questions/37650716/python-fixed-wait-time-for-receiving-socket-data
import time
from socket import socket, SOCK_DGRAM, AF_INET
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
#Client has a 1 second window to attain a message=
clientSocket.settimeout(1)
#Able to send 5 messages to the server and then get them back
for i in range(0, 20):
    message = input('Input lowercase sentence: ')
    start = time.time()
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
    try:
        modifiedMessage, addr = clientSocket.recvfrom(2048)
    except ConnectionError:
        print("Connection between client and server is not working!")
    except OSError:
        print("Timeout! Try again...")
        continue
    end = time.time()
    if message != '':
        print(modifiedMessage, addr)
        rtt = end - start
        print("RTT of Client = " + str(rtt))
clientSocket.close()

#Allow the client to give up if no response has been received within 1 second