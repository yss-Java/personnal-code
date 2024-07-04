import time
from multiprocessing.pool import Pool


# 异步获取进程的执行结果
def task(n):
    print('{}----->start'.format(n))
    time.sleep(1)
    print('{}------>end'.format(n))
    return n ** 2


if __name__ == '__main__':
    p = Pool(4)
    res_list = []
    for i in range(1, 11):
        res = p.apply_async(task, args=(i,))
        res_list.append(res)  # 使用列表来保存进程执行结果
    for re in res_list:
        print(re.get())
    p.close()
