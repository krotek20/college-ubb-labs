import multiprocessing
import socket
import sys


BYTE_ORDER_DICT = {b'\x01': "little", b'\x00': "big"}


def receive_int(conn):
    return socket.ntohl(int.from_bytes(conn.recv(4), sys.byteorder))


def send_int(conn, nr):
    conn.send(socket.htonl(nr).to_bytes(4, sys.byteorder))


def receive_string(conn):
    len = receive_int(conn)
    return conn.recv(len).decode()


def send_string(conn, mesaj):
    to_send = mesaj.encode()
    send_int(conn, len(to_send))
    conn.send(to_send)


def serve_client(conn, addr):
    print(f"Hello, {addr}")
    print(receive_string(conn))
    send_string(conn, "General Kenobi!")
    conn.close()


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} IP port")
        return
    TCP_IP = sys.argv[1]
    TCP_PORT = int(sys.argv[2])
    socketfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketfd.bind((TCP_IP, TCP_PORT))
    socketfd.listen(5)

    process_list = []
    try:
        while True:
            conn, addr = socketfd.accept()
            process_list.append(multiprocessing.Process(target=serve_client, args=(conn, addr)))
            process_list[-1].start()
    except KeyboardInterrupt:
        for process in process_list:
            process.join()
        socketfd.close()


if __name__ == "__main__":
    main()
