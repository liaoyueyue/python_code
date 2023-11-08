import turtle
turtle.setup(600, 400)
turtle.begin_fill()
# 循环画五个线段，构成五角星
for _ in range(5):
    turtle.forward(100)  # 向前移动100个单位
    turtle.right(144)    # 右转144度
turtle.end_fill()
turtle.exitonclick()
