message = '我爱python'
print(type(message))
message = '''我爱
python'''
print(message)
print(type(message))

message = '我爱' \
          'python'
print(message)
print(type(message))
message = '我爱\'python\''
message = "我爱'python'"
message = 'I love python'
print(message[0])
print(message[1])
print(message[3])
message = 'I love python'
print(len(message))  # len() 用来获取字符串长度 13
#print(message[13])

message = 'abcdef'
print(message[0:4:1])  # abcd
message = 'abcdef'
print(message[0:4:2])
message = 'abcdef'
print(message[:4:1])
message = 'abcdef'
print(message[0::1])
message = 'abcdef'
print(message[::1])
message = 'abcdef'
print(message[0:4:])

message = 'abcdef'
print(message[4:0:-1])
message = 'abcdef'
print(message[0:4:-1])
message = 'abcdef'
print(message[-1])
print(message[-2])
message = 'abcdef'
print(message[-4:-1:1])
message = 'abcdef'
print(message[::])
message = 'I love python'
print(len(message))
print(message.find('python',2,12))
message = 'I love python'
print(len(message))
print(message.find('python',2,13))
# message = 'I love python'
# print(message.index('Java'))
message = 'A man who is handsome said that I am a handsome man'
print(message.count('handsome'))
message = 'A man who is handsome said that I am a handsome man'
print(message.count('handsome',18))

message = 'A man who is handsome said that I am a handsome man'
print(message.replace('man','woman',1))
print(message.replace('man','woman',2))

message = 'A man who is handsome said that I am a handsome man'
print(message.replace('man','woman',1))
print(message.replace('man','woman',2))
print(message)

message = 'A man who is handsome said that I am a handsome man'
print(message.split('handsome',1))
print(message.split('handsome',2))
print(type(message.split('handsome',1)))

message = ['我','爱','中国']
print('哈哈'.join(message))

message = ['我','爱','中国']
print(''.join(message))

#字符串序列.capitalize()
message = 'i love python'
print(message.capitalize())

message = 'i love python'
print(message.title())
message = 'I love Python'
print(message.lower())
message = 'I love Python'
print(message.upper())

message = '    I love python    '
print(message.lstrip())

message = '    I love python    '
print(message.rstrip())

message = '    I love python    '
print(message.strip())

message = 'I love python'
print(message.ljust(20,'。'))
message = 'I love python'
print(message.rjust(20,'。'))
message = 'I love python'
print(message.center(20,'。'))


message = 'I love python'
print(message.startswith("I"))
print(message.startswith("love"))

message = 'I love python'
print(message.endswith('python'))
print(message.endswith('python',9,13))

message = 'I love python'
print(message.isalpha())
message = 'abcdef'
print(message.isalpha())


message = '12345'
print(message.isdigit())

message = 'abcdef1234'
print(message.isalnum())
message = 'abcdef'
print(message.isalnum())
message = '      '
print(message.isspace())
