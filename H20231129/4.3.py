# 3.	设计一个Medicin（药品）类，包括药名（name）、价格（price）、生产日期（pd）、失效日期（exp）等属性。将价格、生产日期和失效日期设置为私有属性，不允许随意修改。类需要包括计算保质期的方法guarantee_period()和计算药品是否过期的方法is_expire()。注意：计算保质期会用到datetime对象的day_between函数。

from datetime import datetime

class Medicin:
    def __init__(self, name, price, pd, exp):
        self.__name = name
        self.__price = price
        self.__pd = pd
        self.__exp = exp
    def guarantee_period(self):
        now = datetime.now()
        period = self.__exp - self.__pd
        return period.days
    def is_expire(self):
        now = datetime.now()
        if now > self.__exp:
            return True
        else:
            return False

med1 = Medicin("板蓝根", 10, datetime(2023, 11, 29), datetime(2025, 11, 29))
print("药品名称：", med1._Medicin__name)
print("价格：", med1._Medicin__price)
print("生产日期：", med1._Medicin__pd)
print("失效日期：", med1._Medicin__exp)
print("保质期（天）：", med1.guarantee_period())
print("是否过期：", med1.is_expire())
