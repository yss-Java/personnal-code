import threading

g_num = 0


def test(n):
    global g_num
    for x in range(n):
        g_num = g_num + x
        g_num = g_num - x
    print(g_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=test, args=(10,))
    t2 = threading.Thread(target=test, args=(10,))
    t1.start()
    t2.start()
