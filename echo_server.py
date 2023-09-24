from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))  # combine endpoint and socket
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()  # connection socket, return connection address(IP address port number)
print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)  # receiving data
    if not data:
        break
    print("Received message:", data.decode())  # print received data
    conn.send(data)  # re-send received data to client
conn.close()
