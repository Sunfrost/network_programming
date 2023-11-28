import socket
import sys

port = 2500

s_sock = socket.socket()
host = ''
s_sock.bind((host, port))
s_sock.listen(1)

print("Waiting for connection from a client...")

c_sock, addr = s_sock.accept()
print("Connection from", addr)

msg = c_sock.recv(1024)
print(msg.decode())

filename = input("File name:")

c_sock.send(filename.encode())

with open("./" + filename, 'rb') as f:
    c_sock.sendfile(f, 0)

print("File sending complete.")
c_sock.close()
