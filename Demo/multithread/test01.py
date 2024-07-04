import time
import _thread


def print_time(tag, *var_args, **var_kwargs):
    count = 5
    while count > 0:
        time.sleep(2)
        count -= 1
        print("%s: %s" % (tag, time.ctime()))


# 启动一个新线程, 线程函数为 print_time,
# 其中 args 元祖中的参数将依次传递给线程函数前面的变量, 剩余的组成新元祖传递给 var_args,
# kwargs 字典参数将传递给 var_kwargs, 即结果为:
# tag: "T1"
# var_args: (1, "Hello")
# var_kwargs: {"name": "World", "age": 25}
_thread.start_new_thread(print_time, ("T1", 1, "Hello"), {"name": "World", "age": 25})

# 再启动一个新线程
_thread.start_new_thread(print_time, ("T2",))


while True:
    pass            # 执行完后需要强制退出
