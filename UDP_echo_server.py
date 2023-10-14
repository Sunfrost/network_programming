import socket
port = 3400
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))

while True:
    data, addr = sock.recvfrom(BUFSIZE)
    print("Received message: ", data.decode())
    resp = input(":")
    sock.sendto(resp.encode(), addr)
