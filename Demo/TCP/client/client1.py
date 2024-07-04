"""
TCP 客户端
"""
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 8080))
    s.sendall("你好 Hello".encode("UTF-8"))
    data = s.recv(1024)
    print(data.decode("UTF-8"))
