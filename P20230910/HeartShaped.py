import turtle

turtle.setup(600, 400)
turtle.penup()
turtle.pensize(2)
turtle.goto(0, 90)
turtle.left(135)  # 逆时针转动画笔135度
turtle.begin_fill()
turtle.color("pink", "pink")
turtle.pendown()
turtle.circle(63.65, 180)
turtle.goto(0, -90)
turtle.goto(90, 0)
turtle.setheading(45)  # 调整画笔方向为绝对方向45度
turtle.circle(63.65, 180)
turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

