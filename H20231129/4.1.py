# 1.	设计一个Circle（圆）类，包括半径、颜色等属性，且包括计算其周长和面积的方法。创建Circle类的实例对象，传入其半径和颜色，计算出该实例对象的周长和面积。
import math

class Circle:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def c_perimeter(self):
        return 2 * math.pi * self.r
    def c_area(self):
        return math.pi * self.r ** 2
r = float(input("请输入半径"))
c = input("请输入颜色")
c1 = Circle(r, c)
print("圆的周长为：" + str(c1.c_perimeter()))
print("圆的面积为：" + str(c1.c_area()))
print("圆的颜色为：" + str(c1.c))