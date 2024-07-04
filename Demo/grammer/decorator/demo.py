# def fun(name):
#     member={"count":0}
#     def fun_inner():
#         member["count"]+=1
#         print(name,member["count"])
#     return fun_inner
# f1=fun("hello")
# f2=fun("world")
# f1()
# f1()
# f2()
import time


def exec_time(fun):
    """
        装饰器只有一个参数, 用于接收被装饰的函数对象
        """
    def inner_fun():
        start_time=time.time()
        fun()
        end_time=time.time()
        print("%s use time %d" % (fun.__name__, end_time - start_time))
    return inner_fun
# @exec_time 的作用相当于执行了 test = exec_time(test)
@exec_time
def test():
    print("test_fun()")
    time.sleep(2)
# 经过装饰器装饰后, 这里的 test 函数就不是原来的函数了,
# 而是调用了 exec_time(fun) 方法返回的一个函数
print(test.__name__)
test()
# 调用经过装饰后的 test 方法,
# 实际调用的是 exec_time 内部的 inner_fun
