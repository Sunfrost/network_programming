import socket

port = int(input("Port No: "))
host = 'localhost'
address = (host, port)  # address format -> always (ip, port) tuple
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)  # requesting server connection

while True:
    msg = input("Message to send: ")

    if not msg:
        continue
    try:
        s.send(msg.encode())  # send a message to server
    except:
        print("연결 종료")
        break

    try:
        data = s.recv(BUFSIZE)  # receive a message from server
        if not data:
            print("연결 종료")
            break
        print("Received message: %s" %data.decode())  # convert byte-type data to string
    except:
        print("연결 종료")
        break
s.close()
