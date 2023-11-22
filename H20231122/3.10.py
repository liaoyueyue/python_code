# 10.	用递归的方法求斐波那契数列的第n项。
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 计算第n项斐波那契数列的值
n = 20  # 可以替换为你想要计算的项数
result = fibonacci(n)
print(f"斐波那契数列第{n}项的值为：{result}")
