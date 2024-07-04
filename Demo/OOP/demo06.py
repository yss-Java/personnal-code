# 添加类静态方法，批量创建对角点
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # @staticmethod
    # def create_diag_points(count):
    #     points=[]
    #     for i in range(count):
    #         points.append(Point(i,i,i))
    #     return points
    @classmethod
    def create_diag_points(cls, count):
        # 在@classmethod修饰的方法中，其中 cls 表示 Point
        points = []
        for i in range(count):
            points.append(cls(i, i, i))
        return points


if __name__ == '__main__':
    points = Point.create_diag_points(1000)
