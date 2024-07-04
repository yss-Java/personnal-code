import re



# 实现简易四则运算
def naive_calc(code):
    code_lines = [l for l in code.split('\n') if l.strip() != '']
    for line in code_lines:
        ret = re.match("\s*(\d+)([\+\-\*\/])(\d+)\s*", line)
        left = ret.group(1)
        op = ret.group(2)
        right = ret.group(3)
        if op == '+':
            print('{}+{}={}'.format(left, right, int(left) + int(right)))
        elif op == '-':
            print('{}-{}={}'.format(left, right, int(left) - int(right)))
        elif op == '*':
            print('{}*{}={}'.format(left, right, int(left) * int(right)))
        elif op == '/' and right != '0':
            print('{}/{}={}'.format(left, right, int(left) / int(right)))


def test():
    code = '''
     1+2
    3+4
    5-3
    4*3
    10/2
    88+66
    92*64
    '''
    naive_calc(code)


if __name__ == '__main__':
    test()
