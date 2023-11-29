# 4.	在现实生活中，机动车一般有两种作用，一种是载人，一种是载物，这可能看作两种运行方法。设计程序模拟客车和货车的运行，反映出客车载人数和货车载物数。
# a)	定义车类Car，包括名称属性name，以及运行方法run()
# b)	定义客车类TaxiCar，包括名称属性name,载人属性person_num，以及运行方法run()
# c)	定义货车FreightCar，包括名称属性name,载物属性goods_weight，以及运行方法run()
# d)	创建客车类和货车类的实例对象，并调用其运行方法。

class Car:
    def __init__(self, name):
        self.name = name
    def run(self):
        print(f"{self.name}正在行驶")
class TaxiCar(Car):
    def __init__(self, name, person_num):
        super().__init__(name)
        self.person_num = person_num
    def run(self):
        print(f"我是{self.name}，能载{self.person_num}人行驶")
class FreightCar(Car):
    def __init__(self, name, goods_weight):
        super().__init__(name)
        self.goods_weight = goods_weight
    def run(self):
        print(f"我是{self.name}，能载{self.goods_weight}吨货物行驶")

taxi = TaxiCar("出租车", 4)
truck = FreightCar("货车", 10)
taxi.run()
truck.run()
