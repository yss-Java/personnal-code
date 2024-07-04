import socket

# 创建面向连接（TCP）服务端 Socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定 主机和端口, "" 表示本地所有可用接口
ss.bind(("", 8080))

# 开始监听 客户端 连接
ss.listen()

while True:
    # 阻塞等待接收一个客户端连接, 返回元祖 (客户端socket, 客户端地址)
    # conn: 与客户端建立的 socket 对象
    # addr: 客户端地址, 元祖 (host, port)
    conn, addr = ss.accept()

    # 接收客户端发来的数据
    data = conn.recv(1024)

    # 打印 客户端地址 和 收到的数据
    print("%s: %s" % (addr, data.decode("UTF-8")))

    # 发送数据到客户端
    conn.sendall("收到".encode("UTF-8"))

    # 关闭 客户端 socket
    conn.close()

# 关闭 服务端 Socket
# ss.close()
