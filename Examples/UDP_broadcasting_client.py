from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(('', 7000))

while True:
    msg, addr = sock.recvfrom(1024)
    print(msg.decode())