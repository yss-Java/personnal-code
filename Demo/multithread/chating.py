import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 8000))


def send_msg():
    ip = input('请输入你要聊天的ip：')
    port = int(input('请输入对方的端口号：'))
    while True:
        msg = input('请输入聊天内容')
        s.sendto(msg.encode('utf-8'), (ip, port))
        if msg == "bye":
            ip = input('请输入你要聊天的ip')
            port = int(input('请输入对方的端口号'))


def recv_msg():
    while True:
        content, addr = s.recvfrom(1024)
        print('接收到了{}主机{}端口的消息:{}'.format(addr[0], addr[1], content.decode('utf-8')),
              file=open('history.txt', 'a', encoding='utf-8'))


send_thread = threading.Thread(target=send_msg)
recv_thread = threading.Thread(target=recv_msg)

send_thread.start()
recv_thread.start()
