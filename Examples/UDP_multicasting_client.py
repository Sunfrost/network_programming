from socket import *
import struct

BUFFER = 1024
group_addr = "224.0.0.254"
r_sock = socket(AF_INET, SOCK_DGRAM)
r_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
r_sock.bind(("", 6500))

mreq = struct.pack("4sl", inet_aton(group_addr), INADDR_ANY)
r_sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
print("Ready to receive")

while True:
    rmsg, addr = r_sock.recvfrom(BUFFER)
    print("Received {} from ({}, {})".format(rmsg.decode(), *addr))
    r_sock.sendto('ACK'.encode(), addr)
