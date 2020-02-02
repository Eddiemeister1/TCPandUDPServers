#UDPServer.py
#Assignment #4
#By Eduardo Dotel
#The time portion of the code is credited to the person who answered the question in:
#https://stackoverflow.com/questions/37650716/python-fixed-wait-time-for-receiving-socket-data
import time
import random
from socket import socket, SOCK_DGRAM, AF_INET
#Create a UDP socket
#Noticd the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family forv IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print("Waiting for connections")
while True:
    #Receive the client packet along with the address it is coming from
    start = time.time()
    message, address = serverSocket.recvfrom(2048)
    if random.randint(1, 5) != random.randint(1, 5):
        serverSocket.sendto(message, address)
        end = time.time()
    else:
        print("UDP Packet dropped randomly!")
        continue
    if message != '':
        print(message, address)
        #Capitalize the message from the client
        message = message.upper()
        rtt = end - start
        print("RTT of Server: " + str(rtt))

serverSocket.close()

#Configure the server so that it randomly drops packets
#Include information about how long each response took.
#This will be the RTT.