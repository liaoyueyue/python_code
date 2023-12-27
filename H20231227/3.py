# 使用列表推导式，求从1-4中任选2个数组成的所有2位数。

result = [i*10 + j for i in range(1, 5) for j in range(1, 5) if i != j]
print(result)
