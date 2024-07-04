# 1、被除数为 0，未捕获异常
# def getNum(n):
#         return 10 / n
# print(getNum(0))
# 输出结果：ZeroDivisionError: division by zero

# 2、捕获异常
# def getNum(n):
#     try:
#         return 10 / n
#     except IOError:
#         print('Error: IOError argument.')
#     except ZeroDivisionError:
#         print('Error: ZeroDivisionError argument.')
# print(getNum(0))
def getNum(n):
    try:
        print('try --> ', 10 / n)
    except ZeroDivisionError:
        print('except --> Error: ZeroDivisionError argument.')
    else:
        print('else -->')
    finally:
        print('finally -->')


getNum(0)
getNum(1)
