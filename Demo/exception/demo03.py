class ShortInputException(Exception):
    '''自定义的异常类'''

    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

    def __str__(self):
        return '输入的长度是 %d, 长度至少应是 %d' % (self.length, self.atleast)


def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise 引发一个自定义的异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:
        print('ShortInputException:', result)
    else:
        print('没有异常发生.')


if __name__ == '__main__':
    main()
