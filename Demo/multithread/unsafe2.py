import threading
import time

ticket = 20


def sell_ticket():
    global ticket
    while True:
        if ticket > 0:
            time.sleep(0.5)
            ticket = ticket - 1
            print('{}卖了一张票，还剩{}'.format(threading.current_thread().name, ticket))
        else:
            print('{}票卖完了'.format(threading.current_thread().name))
            break


for i in range(5):
    t = threading.Thread(target=sell_ticket, name='thread-{}'.format(i + 1))
    t.start()

if __name__ == '__main__':
    sell_ticket()

