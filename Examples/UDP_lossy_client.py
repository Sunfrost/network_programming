import socket

BUFFER = 1024
port = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', port))

for i in range(10):
    delay = 0.1
    data = "Hello message"
    while True:
        sock.send(data.encode())
        print("Waiting up to {} seconds for a reply".format(delay))
        sock.settimeout(delay)
        try:
            data = sock.recv(BUFFER)
        except socket.timeout:
            delay *= 2
            if delay > 2.0:
                break
        else:
            print("Response: ", data.decode())
            break
