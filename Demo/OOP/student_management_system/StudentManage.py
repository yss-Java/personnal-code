from Student import *
class student_manage(object):

    def __init__(self):
        self.student_list = []
    def menu(self):
        print("欢迎来到学员管理系统")
        print("1.增加学员信息")
        print("2.删除学员信息")
        print("3.修改学员信息")
        print("4.查找学员信息")
        print('5.显示所有学员信息')
        print("6.保存学员信息")
        print("0.退出学员管理系统")
        print()

    def add_student(self):
        student_name = input('请输入学员姓名:')
        student_gender = input('请输入学员性别:')
        student_tel = input('请输入学员电话:')
        for i in self.student_list:
            if i.name == student_name:
                print('对不起，该学员信息已存在')
                break
        else:
            new_student = Student(student_name, student_gender, student_tel)
            self.student_list.append(new_student)
            print('添加成功')


    def delete_student(self):
        del_name = input('请输入你要删除的学员的姓名:')
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                print('删除成功')
                break
        else:
            print('该学员不存在，删除失败')

    def modify_student(self):
        modify_name = input('请输入你要修改的学员的姓名:')
        modify_tel = input('请输入你要修改的学员的电话:')
        for i in self.student_list:
            if i.name == modify_name:
                i.tel = modify_tel
                print('修改成功')
                break;
        else:
            print('对不起，学员信息不存在，修改失败')

    def search_student(self):
        student_name = input('请输入你要查找的学员的姓名:')
        for i in self.student_list:
            if i.name == student_name:
                print(f'姓名\t性别\t电话')
                print(i)
                break
        else:
            print('你要查找的学员不存在')

    def print_student(self):
        print('姓名\t性别\t电话')
        for i in self.student_list:
            print(i)

    def save_student(self):
        f = open('student.data','w')
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))
        f.close()
        print('保存成功')

    def load_student(self):
        try:
            f = open('student.data','r')
        except Exception as result:
            print(result)
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'],i['gender'],i['tel']) for i in new_list]
        finally:
            f.close()

    def run(self):
        self.load_student()
        while True:
            self.menu()
            opt = input('请输入要执行的操作的序号:')
            if opt == '1':
                self.add_student()
            elif opt == '2':
                self.delete_student()
            elif opt == '3':
                self.modify_student()
            elif opt == '4':
                self.search_student()
            elif opt == '5':
                self.print_student()
            elif opt == '6':
                self.save_student()
            else:
                break
