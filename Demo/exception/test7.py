# 自定义异常类 MyExc
class MyExc(Exception):  # 继承Exception类
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 0:
            return '被除数不能为0'


# 自定义方法
def getNum(n):
    try:
        if n == 0:
            exc = MyExc(n)
            print(exc)
        else:
            print(10 / n)
    except:
        pass


if __name__ == '__main__':
    getNum(1)
    getNum(0)
