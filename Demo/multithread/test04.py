import threading


def thread_run(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    print(threading.current_thread().getName())


# 创建线程, 并启动, 启动后 thread_run 将被调用
threading.Thread(
    target=thread_run,
    args=("Hello", 3.14),
    kwargs={"name": "World", "age": 20}
).start()
