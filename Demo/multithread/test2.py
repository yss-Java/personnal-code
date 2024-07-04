import threading
import _thread
import time

# 创建一个线程本地数据对象, mydata 对象在不同的线程中将会有不同的实例
mydata = threading.local()

# 在主线程中把 mydata.x 赋值为 1
mydata.x = 1


def thread_func():
    # 在子线程中把 mydata.x 赋值为 2
    mydata.x = 2


# 启动一个子线程（在子线程中把 mydata.x 赋值为 2）
_thread.start_new_thread(thread_func, ())

# 稍作延时, 等待子线程退出
time.sleep(3)

# 在主线程中获取的 mydata.x 的值将仍然为 1
print(mydata.x)
