import threading
import time

# 创建条件对象, 自动创建底层锁
cond = threading.Condition()


class MyThread01(threading.Thread):
    def run(self):
        cond.acquire()  # 阻塞, 直至获取到底层锁
        try:
            cond.wait()  # 阻塞并释放底层锁, 直至被其他线程 notify 唤醒,
            # 唤醒后需要重新竞争获取到底层锁后才能结束阻塞
            print("MyThread01")
        finally:
            cond.release()  # 释放底层锁


class MyThread02(threading.Thread):
    def run(self):
        cond.acquire()  # 阻塞, 直至获取到底层锁
        try:
            time.sleep(3)
            cond.notify_all()  # 唤醒所有在此条件对象上等待的线程
            print("MyThread02")
        finally:
            cond.release()  # 释放底层锁


# 创建线程
t1 = MyThread01()
t2 = MyThread02()

# 启动线程
t1.start()
t2.start()
