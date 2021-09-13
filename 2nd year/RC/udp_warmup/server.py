import socket
import sys


def receive_int(s):
    nr, addr = s.recvfrom(4)
    return socket.ntohl(int.from_bytes(nr, sys.byteorder)), addr


def send_int(s, addr, nr):
    to_send = socket.htonl(nr).to_bytes(4, sys.byteorder)
    s.sendto(to_send, addr)


def receive_string(s):
    msg_len, addr1 = receive_int(s)
    msg, addr2 = s.recvfrom(msg_len)
    return msg.decode(), addr2


def send_string(s, addr, mesaj):
    send_int(s, addr, len(mesaj))
    s.sendto(mesaj.encode(), addr)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IP_UDP = ""
    PORT_UDP = 1234
    s.bind((IP_UDP, PORT_UDP))
    mesaj, addr = receive_string(s)
    print(mesaj)
    send_string(s, addr, "general kenobi")


if __name__ == "__main__":
    main()
