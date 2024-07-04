"""
TCP 服务端
"""
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
    ss.bind(("", 8080))
    ss.listen()
    while True:
        conn, addr = ss.accept()
        with conn:
            data = conn.recv(1024)
            print("%s: %s" % (addr, data.decode("UTF-8")))
            conn.sendall("收到".encode("UTF-8"))
