class PasswordError(Exception):
    def __int__(self, input):
        self.input = input

    def __str__(self):
        return f'你输入的密码{self.input}与正确密码不符'


def login():
    password = '987654'
    while True:
        try:
            input_password = input('请输入密码:')
            if password != input_password:
                raise PasswordError(input_password)
        except Exception as result:
            print(result)
        else:
            print('登录成功')
            break


login()
