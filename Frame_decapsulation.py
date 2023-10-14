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