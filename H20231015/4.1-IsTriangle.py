def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = float(input("请输入第一条边的长度: "))
b = float(input("请输入第二条边的长度: "))
c = float(input("请输入第三条边的长度: "))

if is_triangle(a, b, c):
    print("可以构成三角形")
else:
    print("不能构成三角形")
