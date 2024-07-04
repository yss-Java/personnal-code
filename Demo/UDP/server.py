import socket
# 创建面向非连接（UDP）服务端 Socket
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定 主机和端口, "" 表示本地所有可用接口
ss.bind(("",8080))
while True:
    # 阻塞等待接收客户端发来的数据, 返回元祖 (数据, 客户端地址)
    data,address = ss.recvfrom(1024)
    # 打印 客户端地址 和 收到的数据
    print("%s: %s" % (address, data.decode("UTF-8")))
    # 回复数据到客户端（连接必须还没有关闭）
    ss.sendto("收到".encode("UTF-8"), address)

# 关闭 服务端 Socket
# ss.close()
