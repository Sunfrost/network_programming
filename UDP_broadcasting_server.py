import socket
from socket import *

addr = ('<broadcast>', 7000)

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    smsg = input("Broadcast message: ")
    sock.sendto(smsg.encode(), (addr))