import turtle as t

t.setup(1920, 1080)
t.pensize(3)
t.colormode(255)
t.pencolor((51, 9, 5))
t.speed(0)

t.hideturtle()


def drawOutline():
    # 画左耳朵
    t.fillcolor((254, 226, 90))
    t.begin_fill()
    t.penup()
    t.goto(-190, 206)
    t.pendown()
    t.setheading(-35)
    t.circle(475, -34)
    t.setheading(169.5)
    t.circle(360, -46)

    t.seth(22)
    t.circle(-260, 42.5)

    # 画右耳朵
    t.seth(57.5)
    t.circle(-300, 56)
    t.seth(252)
    t.circle(-340, 45)

    t.seth(-61)
    t.circle(-260, 32)
    t.seth(-70)
    t.circle(-260, 10)

    # 尾巴
    t.seth(45)
    t.circle(-480, 40)
    t.seth(-104)
    t.forward(248)
    t.seth(176)
    t.forward(165)
    t.seth(-64)
    t.forward(112)
    t.seth(-158)
    t.forward(68)

    # 右脚
    t.seth(-82)
    t.circle(-100, 20)
    t.circle(-400, 15)
    t.circle(-100, 25)
    t.circle(-9, 130)

    # 底部
    t.seth(-142)
    t.circle(-100, 50)
    t.left(9)
    t.circle(400, 5)
    t.right(11)
    t.circle(480, 20)
    t.right(7)
    t.circle(-100, 37)

    # 左脚
    t.left(80)
    t.circle(-12, 80)
    t.left(15)
    t.circle(-70, 50)
    t.left(6.5)
    t.circle(-500, 12)
    t.right(3)
    t.circle(-70, 30)
    t.right(30)
    t.circle(-18, 80)
    t.circle(-100, 20)

    # 左边身体
    t.left(155)
    t.circle(-30, 80)
    t.left(76)
    t.circle(-130, 47)
    t.right(75)
    t.circle(100, 4)
    t.circle(100, -93)
    t.right(150)
    t.circle(-260, 32)
    t.goto(-190, 206)
    t.end_fill()


drawOutline()

# 左耳朵咖啡色部分
t.fillcolor((51, 9, 5))
t.penup()
t.goto(-288, 299)
t.begin_fill()
t.circle(-140, 40)
t.right(58)
t.circle(-360, -25.5)
t.right(58)
t.circle(475, 17.8)
t.end_fill()

# 右耳朵咖啡色部分
t.goto(173, 375)
t.left(10)
t.begin_fill()
t.circle(-200, 31.2)
t.left(118)
t.circle(340, 25)
t.left(110)
t.circle(300, 27)
t.end_fill()

t.goto(183, 31)
t.pendown()
t.left(73)
t.circle(-98, 75)
t.circle(-98, -7)

t.fillcolor('white')
t.begin_fill()
t.left(90)
t.circle(-180, 34)
t.circle(-180, -4)
t.left(135)
t.forward(80)
t.left(83)
t.forward(80)
t.left(110)
t.circle(-98, 25)
t.end_fill()

t.penup()
t.goto(171, -172)
t.pendown()
t.left(79)
t.fd(46)
t.left(149)
t.circle(-50, 70)
t.right(50)
t.circle(-40, 40)
t.penup()
t.goto(163, -348)
t.pendown()
t.right(181)
t.circle(-200, 15)
t.right(5)
t.circle(-200, 25)

t.penup()
t.goto(-183, -352)
t.pendown()
t.left(20)
t.circle(100, 20)
t.left(5)
t.circle(300, 25)

# 鼻子和嘴巴
t.penup()
t.goto(-26, 15)
t.dot(7, (50, 19, 0))
t.goto(-24, -9)
t.pendown()
t.seth(-90)
t.left(44)
t.circle(29, 88)
t.circle(29, -88)
t.right(88)
t.circle(-29, 88)

# 左手
t.penup()
t.goto(-137, -119)
t.pendown()
t.right(155)
t.circle(-100, 40)
t.left(10)
t.circle(-130, 18)
t.left(25)
t.forward(11)
t.right(30)
t.circle(-5, 90)
t.circle(5, 110)
t.right(50)
t.circle(-8, 90)
t.left(90)
t.forward(10)
t.right(80)
t.circle(-260, 23)

# 右手
t.penup()
t.goto(128, -197)
t.pendown()
t.left(55)
t.circle(-200, 27)
t.left(45)
t.circle(-10, 90)
t.forward(16)
t.right(50)
t.forward(9)
t.left(60)
t.forward(14)
t.right(80)
t.circle(-200, 30)

# 左眼
t.penup()
t.goto(-153, 77)
t.pendown()
t.seth(83)
t.fillcolor((47, 8, 0))
t.begin_fill()
t.circle(-33, 360)
t.end_fill()
t.penup()
t.goto(-128, 86)
t.dot(32, (254, 254, 252))
t.goto(-121, 71)
t.dot(10, (254, 254, 252))

# 右眼
t.penup()
t.goto(40, 77)
t.pendown()
t.seth(83)
t.fillcolor((47, 8, 0))
t.begin_fill()
t.circle(-33, 360)
t.end_fill()
t.penup()
t.goto(65, 86)
t.dot(32, (254, 254, 252))
t.goto(72, 71)
t.dot(10, (254, 254, 252))

# 右腮红
t.goto(96, 1)
t.pendown()
t.left(10)
t.fillcolor((236, 93, 64))
t.begin_fill()
t.circle(-45, 360)
t.end_fill()

# 左腮红
t.penup()
t.goto(-144, 1)
t.pendown()
t.fillcolor((236, 93, 64))
t.begin_fill()
t.circle(45, 360)
t.end_fill()

# 下巴
t.penup()
t.goto(10, -96)
t.pendown()
t.fillcolor((233, 170, 55))
t.pencolor((233, 170, 55))
t.left(100)
t.begin_fill()
t.circle(-130, 26)
t.circle(5, 180)
t.right(40)
t.circle(40, 110)
t.circle(5, 180)
t.end_fill()

t.done()
