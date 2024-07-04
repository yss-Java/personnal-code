# 创建学生类, 创建一个学生列表，加入3个学生，循环打印学生信息
# 方式一
class Student:
    # 初始化成员
    def __init__(self, no, name, age):
        self.no = no
        self.name = name
        self.age = age

    # 打印信息
    def dump(self):
        infos = [
            f"* no:{self.no}",
            f"* name:{self.name}",
            f"* age:{self.age}"
        ]
        for info in infos:
            print(info)


if __name__ == '__main__':
    students = []
    for i in range(0, 3):
        s = Student(i, f'somebody_{i}', 20 + i)
        students.append(s)
    for s in students:
        print('')
        s.dump()
