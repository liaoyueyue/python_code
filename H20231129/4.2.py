# 2.	设计一个House（房子）类，包括房子名称、长、宽等属性，同时包括计算房子面积的方法，并设置类属性用于计算房子的总数。创建House类的多个实例对象，传入其长和宽，计算出房子的总数和每个房子的面积。
class House:
    count = 0
    def __init__(self, long, wide):
        self.long = long
        self.wide = wide
        House.count = House.count + 1
    def area(self):
        return self.long * self.wide
h1 = House(2, 2)
print(f"房子1, 长为{h1.long}, 宽为{h1.wide}, 面积为{h1.area()}, 房子总数为：{h1.count}")
h2 = House(2, 4)
print(f"房子2, 长为{h2.long}, 宽为{h2.wide}, 面积为{h2.area()}, 房子总数为：{h2.count}")
h3 = House(3, 3)
print(f"房子3, 长为{h3.long}, 宽为{h3.wide}, 面积为{h3.area()}, 房子总数为：{h3.count}")

