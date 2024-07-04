from multiprocessing import Process, Pool
import time


def task(n):
    print('{}----->start'.format(n))
    time.sleep(1)
    print('{}------>end'.format(n))
    return n ** 2


if __name__ == '__main__':
    p = Pool(4)
    for i in range(1, 11):
        res = p.apply_async(task, args=(i,))  # `res` 是任务的执行结果
        print(res.get())  # 直接获取结果的弊端是，多任务又变成同步的了
    p.close()
    # p.join()  不需要再`join`了，因为 `res.get()`本身就是一个阻塞方法
