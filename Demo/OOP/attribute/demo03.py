class Account():
    Account_name = '1234567'
    __Account_password = '987654'

    @classmethod
    def get_password(cls):
        return cls.__Account_password


result1 = Account.get_password()
print(result1)  # 987654
account1 = Account()
result2 = account1.get_password()
print(result2)  # 987654
