# 9.	编写一个函数，用于计算多个数字的乘积，参数的个数不确定，计算后返回乘积。
def calculate_product(*args):
    if not args:
        return None  # 如果没有参数传入，返回 None 或者你认为合适的默认值

    product = 1
    for num in args:
        product *= num
    return product

# 示例调用函数
result = calculate_product(2, 3, 4)
print(f"乘积为：{result}")

result2 = calculate_product(1, 2, 3, 4, 5)
print(f"乘积为：{result2}")
