import threading
import time


class MyThread(threading.Thread):
    """
    自定义一个线程类, 继承线程基类
    """

    def run(self):
        """
        启动线程后, run() 方法将在该线程中被调用
        """
        time.sleep(1)
        print(self.getName())


# 创建两个线程对象
t1 = MyThread()
t2 = MyThread()

# 启动线程
t1.start()
t2.start()
