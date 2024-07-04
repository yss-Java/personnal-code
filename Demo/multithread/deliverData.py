import threading
import time
from queue import Queue


# 生产者函数，用于将数据放入队列中
def producer(queue):
    for i in range(100):
        print('{}存入了{}'.format(threading.current_thread().name, i))
        queue.put(i)
        time.sleep(0.1)


# 消费者函数，用于从队列中取出数据
def consumer(queue):
    for x in range(100):
        value = queue.get()
        print('{}取到了{}'.format(threading.current_thread().name, value))
        time.sleep(0.1)
        if not value:
            return


if __name__ == '__main__':
    # 创建一个队列对象
    queue = Queue()
    # 创建多个线程，并将队列对象作为参数传递给线程函数
    t1 = threading.Thread(target=producer, args=(queue,))
    t2 = threading.Thread(target=consumer, args=(queue,))
    t3 = threading.Thread(target=consumer, args=(queue,))
    t4 = threading.Thread(target=consumer, args=(queue,))
    t5 = threading.Thread(target=consumer, args=(queue,))

    # 启动线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
