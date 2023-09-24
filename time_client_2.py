import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)
sock.connect(address)  # connect to server
print("Current time:", sock.recv(1024).decode())  # convert received message to string then print
