import threading
import time

ticket = 20
lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:
        lock.acquire()
        if ticket > 0:
            time.sleep(0.5)
            ticket -= 1
            lock.release()
            print('{}卖了一张票，还剩{}'.format(threading.current_thread().name, ticket))
        else:
            print('{}票卖完了'.format(threading.current_thread().name))
            lock.release()
            break


for i in range(5):
    t = threading.Thread(target=sell_ticket, name='thread-{}'.format(i + 1))
    t.start()
