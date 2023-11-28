import socket

s_sock = socket.socket()
host = 'localhost'
port = 2500

s_sock.connect((host, port))

s_sock.send("I am ready".encode())

fn = s_sock.recv(1024).decode()

with open("./"+"recv", 'wb') as f:
    print("Receiving...")
    while True:
        data = s_sock.recv(8192)
        if not data:
            break
        f.write(data)

print("File download complete.")
s_sock.close()
