from multiprocessing import Process, Pool
import time


def task(n):
    print('{}----->start'.format(n))
    time.sleep(1)
    print('{}------>end'.format(n))


if __name__ == '__main__':
    p = Pool(8)  # 创建进程池，并指定进程池的个数，默认是CPU的核数
    for i in range(1, 11):
        # p.apply(task, args=(i,))  # 同步执行任务，一个一个地执行任务，没有并发效果
        p.apply_async(task, args=(i,))  # 异步执行任务，可以达到并发效果
    p.close()
    p.join()
