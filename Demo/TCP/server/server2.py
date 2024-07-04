"""
Socket 服务器 代码示例
"""


import socket
import time


socket_server = socket.socket()
# 为 socket 实例对象 绑定 IP 地址和端口号
# IP 地址是字符串类型, 端口号是 int 类型, 将这两个数据定义到元组中
socket_server.bind(('127.0.0.1', 8090))

# 服务器端监听端口
# 传入的参数是一个整数 , 该参数表示允许连接的数量
# 如果连接已满后面的连接请求会等待
socket_server.listen(100)

while True:
    # 4. 阻塞等待连接 , 如果没有客户端连接 , 会一直阻塞在这里
    # accept 函数返回的是 二元元组 , 使用两个变量接收该元组
    # conn 是连接的 socket 对象
    # address 是连接的 地址
    client_socket, client_address = socket_server.accept()
    # 向客户端发送连接成功提示
    client_socket.send('你好，客户端'.encode('UTF-8'))
    print(f'客户端连接成功{client_address}')

    # 5. 服务器端与客户端进行交互
    while True:
        # 循环接收客户端数据, 并使用 UTF-8 解码
        data = client_socket.recv(1024).decode('UTF-8')
        # 向客户端发送消息
        client_socket.send(f'服务端已收到:{data}'.encode())
        print(f'客户端：{data}')
        if data == 'quit':
            break

    # 关闭连接
    client_socket.close()
    print(f'客户端连接关闭{client_address}')
