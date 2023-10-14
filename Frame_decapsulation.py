import socket
import Frame_encapsulation
SIZE = 5

sock = socket.socket()
sock.connect(('localhost', 2800))

HEAD = 0x05
addr = 1
seqNo = 1
frame_seq = ""
msg = "Hello World"
print("전송 메시지", msg)

for i in range(0, len(msg), SIZE):
    frame_seq += Frame_encapsulation.frame(HEAD, addr, seqNo, msg[i:i+SIZE])
    seqNo += 1

sock.send(frame_seq.encode())
msg = sock.recv(1024).decode()
print("수신", msg)

r_frame = msg.split(chr(0x05))
del r_frame[0]
p_msg = ''
for field in r_frame:
    p_msg += field[10:(11 + int(field[6:10]))]

print("복원 메시지:", p_msg)
sock.close()


def frame(start_ch, addr, seqNo, msg):
    addr = str(addr).zfill(2)
    seqNo = str(seqNo).zfill(4)
    length = str(len(msg)).zfill(4)
    return chr(start_ch) + addr + seqNo + length + msg

if __name__ == '__main__':
    stat_ch = 0x05
    addr = 2
    seqNo = 1

    msg = input("Your message:")
    capsule = frame(start_ch=stat_ch, addr=addr, seqNo=seqNo, msg=msg)
    print(capsule)
