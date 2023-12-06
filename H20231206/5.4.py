# 4.	已知random模块中的sample()函数功能为选择多个不重复的随机元素，通过列表推导式产生data数据data = [sample(range(100), 5) for i in range(5)],说明以下两个语句段的功能。
# for row in filter(lambda row: sum(row) % 2 == 0, data):
#             print(row)
# for row in sorted(data, key=lambda row:row[1]):
#     print(row)

# 第一个
# 这个语句段的作用是从data列表中筛选出所有元素之和为偶数的子列表，并打印出来。filter()
# 函数接受一个函数和一个可迭代对象作为参数，返回一个迭代器，其中包含满足该函数条件的元素。在这里，lambda row: sum(row) % 2 == 0
# 是一个匿名函数，用于判断子列表的元素之和是否为偶数。

# 第二个
# 这个语句段的作用是对data列表进行排序，并按照每个子列表的第二个元素进行升序排列。
# sorted()函数接受一个可迭代对象和一个可选的关键字参数key，用于指定排序依据。
# 在这里，lambda row:row[1]是一个匿名函数，用于提取每个子列表的第二个元素作为排序依据。