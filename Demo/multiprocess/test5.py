from multiprocessing import Process
import os

nums = [11, 22]


def work1():
    """子进程要执行的代码"""
    print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))
    for i in range(3):
        nums.append(i)
        print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))


def work2():
    """子进程要执行的代码"""
    nums.pop()
    print("in process2 pid=%d ,nums=%s" % (os.getpid(), nums))


if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()
    p1.join()

    p2 = Process(target=work2)
    p2.start()

    print('in process0 pid={} ,nums={}'.format(os.getpid(), nums))
