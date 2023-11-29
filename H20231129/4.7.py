"""
7.	扩展训练：模拟大象装进冰箱的问题。在此训练中需要注意，一个类中的对象是可以传入另一个类中使用的。需要进行以下操作。
a)	定义一个Elphant类，包括名称属性name、打开冰箱方法open()、关闭冰箱方法close()、进入冰箱方法enter().
b)	定义Fridge类，包括名称属性name、打开门方法open_door()和关闭门方法close_door()。两个方法中要传入进冰箱的大象名称。
c)	模拟大象进冰箱的过程：打开冰箱门，进入冰箱，关闭冰箱门。
"""

class Elphant:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f"{self.name}打开了冰箱门")

    def close(self):
        print(f"{self.name}关闭了冰箱门")

    def enter(self):
        print(f"{self.name}进入了冰箱")


class Fridge:
    def __init__(self, name):
        self.name = name

    def open_door(self, elephant_name):
        print(f"{elephant_name}打开了冰箱门")

    def close_door(self, elephant_name):
        print(f"{elephant_name}关闭了冰箱门")


elephant = Elphant("大象")
fridge = Fridge("冰箱")
fridge.open_door(elephant.name)
elephant.enter()
fridge.close_door(elephant.name)
