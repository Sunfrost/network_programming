import socket
BUFSIZE = 1024
port = 3400

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input()
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFSIZE)
    print("Server says: ", data.decode())
