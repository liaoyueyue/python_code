# 3.	创建一个列表，包含1到10的整数，使用map()函数和匿名函数来将偶数元素乘以2，奇数元素乘以3。输出列表元素。

# 创建一个列表，包含1到10的整数
numbers = list(range(1, 11))

# 使用map()函数和匿名函数来将偶数元素乘以2，奇数元素乘以3
result = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, numbers))

# 输出列表元素
print(result)
