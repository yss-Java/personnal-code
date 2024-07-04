import socket

# 创建TCP socket对象
import time

# 1. 创建 socket 实例对象
client_socket = socket.socket()

# 2. 客户端连接服务器, IP 地址和端口号放在元组中
client_socket.connect(('127.0.0.1', 8090))
# 3. 向服务器端发送消息和接收消息
# 发送数据到服务器
client_socket.send('你好，服务器！'.encode())
print("客户端发送：你好，服务器！")

time.sleep(1)
# 接收服务器数据
data = client_socket.recv(1024).decode("UTF-8")
print(f'服务端：{data}')

# 获取命令行输入发送给客户端
while True:
    command = input("请输入：")
    client_socket.send(command.encode())
    print(f"客户端发送：{command}")
    if command == 'quit':
        break
    # 接收服务器数据
    data = client_socket.recv(1024).decode("UTF-8")
    print(f"服务器：{data}")
# 关闭连接
client_socket.close()
print("客户端关闭")
