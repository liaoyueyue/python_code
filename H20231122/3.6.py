# 6.	自定义一个函数，计算指定边长正方形图中阴影部分的面积。 正方形边长4.5，阴影部分面积为正方形面积减去弧度为90度，弧长为4.5的扇形
import math

def calculate_shadow_area(square_side):
    # 计算正方形的面积
    square_area = square_side * square_side

    # 计算扇形的面积
    radius = square_side / 2  # 正方形的边长的一半作为扇形的半径
    arc_length = square_side  # 弧长等于正方形的边长
    sector_area = 0.5 * radius * radius * math.radians(90)  # 扇形面积公式：0.5 * r^2 * θ，这里角度为90度

    # 计算阴影部分的面积（正方形面积减去扇形面积）
    shadow_area = square_area - sector_area

    return shadow_area

# 正方形边长
side_length = 4.5

# 计算阴影部分的面积
result = calculate_shadow_area(side_length)
print(f"阴影部分的面积为：{result}")
