import threading
import time


# 创建事件对象
event = threading.Event()


class MyThread01(threading.Thread):
    def run(self):
        event.wait()            # 阻塞, 直到事件标记被设置为 True
        print("MyThread01")


class MyThread02(threading.Thread):
    def run(self):
        time.sleep(5)
        event.set()
        # 将事件对象标记设置为 True, 唤醒所有在此事件上等待的线程
        print("\n")
        print("MyThread02")



# 创建线程
t1 = MyThread01()
t2 = MyThread02()

# 启动线程
t1.start()
t2.start()
