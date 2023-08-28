# import keyword
# print(keyword.kwlist)
#
# num = int(input("Please enter a value for num\n"))
#
# if 100 < num:
#     print(f"{num} > 100")
# elif 100 == num:
#     print("100 = 100")
# else:
#     print(f"{num} < 100")

# 1
x = 19
square_sum = eval("x**2")
print(f"{x}的平方为", square_sum, sep=":")


# 2
import random
print("随机数：", random.randint(0, 100))

# 3.爱心
import turtle
turtle.setup(600, 400)
turtle.pensize(2)
turtle.penup()
turtle.goto(0, 90)
turtle.left(135)
turtle.begin_fill()
turtle.color("pink", "pink")
turtle.pendown()
turtle.circle(63.65, 180)
turtle.goto(0, -90)
turtle.goto(90, 0)
turtle.setheading(45)
turtle.circle(63.65, 180)
turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

