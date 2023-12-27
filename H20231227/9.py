# 创建一个Point类，它表示某个点的X和Y坐标的有序数值对。X和Y的值在实例化是传入到构造器。如果缺失某个坐标值，则自动设置为0。重写__str__函数，将X和Y的值以(X,Y)显示出来。。

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
p1 = Point(3, 4)
print(p1)
# 缺失某个坐标值 输出：(0, 0)
p2 = Point()
print(p2)
