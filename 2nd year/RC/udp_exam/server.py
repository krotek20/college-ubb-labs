import socket
import sys
import random


HOST = ""
PORT = 1234


def handle_connection(s, addr):
    print(f"Hello client {addr}")

    message = "Connected to server!"
    to_send_int = socket.htonl(len(message)).to_bytes(4, sys.byteorder)
    s.sendto(to_send_int, addr)
    s.sendto(message.encode(), addr)

    while True:
        n = random.randint(1, 100)
        if n % 2 == 1:
            break
    send_n = socket.htonl(n).to_bytes(4, sys.byteorder)
    s.sendto(send_n, addr)
    print(f"Magic square should have {n} rows and columns")

    magic_square = []
    for i in range(n):
        line = []
        for j in range(n):
            x, addr = s.recvfrom(4)
            x = socket.ntohl(int.from_bytes(x, sys.byteorder))
            line.append(x)
        magic_square.append(line)

    while True:
        L, addr = s.recvfrom(4)
        L = socket.ntohl(int.from_bytes(L, sys.byteorder))
        C, addr = s.recvfrom(4)
        C = socket.ntohl(int.from_bytes(C, sys.byteorder))
        position = magic_square[L][C]
        to_send_position = socket.htonl(position).to_bytes(4, sys.byteorder)
        s.sendto(to_send_position, addr)


with (socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as server:
    server.bind((HOST, PORT))
    while True:
        nr, addr = server.recvfrom(4)
        handle_connection(server, addr)
