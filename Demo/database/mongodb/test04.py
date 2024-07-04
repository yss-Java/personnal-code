from pymongo import MongoClient
import time

client = MongoClient("mongodb://192.168.88.100:27017/")
db = client.admin


def monitor_performance():
    while True:
        # 获取服务器状态
        server_status = db.command("serverStatus")
        print(server_status)

        # 获取当前操作
        current_ops = db.current_op()
        print(current_ops)

        # 每分钟执行一次
        time.sleep(60)


if __name__ == "__main__":
    monitor_performance()
