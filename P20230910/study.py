a = 0b10010
print("二进制", a, sep=":")
b = 0o22
print("八进制", b, sep=":")
c = 18
print("十进制", c, sep=":")
d = 0x12
print("十六进制", d, sep=":")

##############################

import math
print(math.pi)

print(eval("a**b"))

##############################

# format()方法
print("{}年的{}学期我学习了{}这门课程".format(2023, "上", "Python"))
print("{1}年的{0}学期我学习了{2}这门课程".format("上", 2023, "Python"))
# 填充、对齐与宽度格式处理
name = "张三"
studentId = "20230910"
# 使用-占位，宽度为10，姓名和学号居中
print("我叫{0:-^10}, 学号为{1:-^10}".format(name, studentId))
# 分隔符、精度与类型格式处理
# 格式化输出运动时长和消耗卡路里
exercise = 300  # exercise 行使；运动；锻炼；练习；
calories = 3120.123638  # calories 卡路里(热量单位，或一克水升高1摄氏度时所需要的热量)；大卡，千卡(测量食物含热量的单位)
print("卡路里为{0:*>20,}".format(calories)) # 将calories用逗号分隔，并居右侧
# 将exercise转换为一位精度的浮点数，并设置calories的精度为两位
print("我运动了{0:.1f}分钟, 消耗了{1:,.2f}卡路里".format(exercise, calories))

##############################

# f字符串
name = "张三"
studentId = "20230910"
print(f"我叫{name},我的学号是{studentId}")
# 格式化输出
milk = "牛奶"
milk_sales = 100032894.37298
f_milk = f"商品{milk:*^10}, 销售额为{milk_sales:*^20,.2f}"
oil = "食用油"
oil_sales = 100145894.445644
f_oil = f"商品{oil:*^10}, 销售额为{oil_sales:*^20,.3f}"
print(f_milk)
print(f_oil)






