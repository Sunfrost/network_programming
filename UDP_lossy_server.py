from socket import *
import random
port = 3000
BUFFER = 1024
s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print("Listening...")

while True:
    data, address = s_sock.recvfrom(BUFFER)
    if random.randint(1, 10) < 4:
        print("Packet from {} lost!".format(address))
        continue
    print("Message is {!r} from {}".format(data.decode(), address))

    s_sock.sendto('ACK'.encode(), address)
