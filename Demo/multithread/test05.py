import threading
import time

# 创建一个重入锁对象
lock = threading.RLock()


class MyThread(threading.Thread):
    def run(self):
        lock.acquire()              # 获取锁
        try:
            # SYNC BLOCK            # 执行需要同步的相关代码
            time.sleep(5)
        finally:
            lock.release()          # 释放锁


# 创建两个线程对象
t1 = MyThread()
t2 = MyThread()

# 启动线程
t1.start()
t2.start()
