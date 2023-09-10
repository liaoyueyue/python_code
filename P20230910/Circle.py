import turtle

# 设置画布
turtle.setup(400, 300)
turtle.penup()
turtle.pensize(2)
turtle.goto(0, -25)
turtle.begin_fill()  # 填充图形
turtle.color("gold", "gold")  # 设置画笔和填充的颜色都为金色
turtle.circle(50)
turtle.end_fill()  # 结束填充图形
turtle.hideturtle()  # 隐藏画笔形状; hide 隐藏
turtle.exitonclick()  # 绘制完成后不关闭画布，使用鼠标点击退出
