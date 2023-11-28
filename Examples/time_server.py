import socket  # loading socket module
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5000)  # '' = random address, port number = 5000
s.bind(address)  # bind socket and address
s.listen(5)  # waiting for connection, accepting up to 5 connections simultaneously

while True:
    client, addr = s.accept()  # allow connection, return (client socket, rem_addr)
    print("Connection requested from", addr)
    client.send(time.ctime(time.time()).encode())  # transmit current time
    client.close()  # quit socket
