import turtle as t

t.setup(1920, 1080)
t.bgpic('../img/皮卡丘.png')
t.dot(5, (0, 0, 0))
t.pensize(3)
t.colormode(255)
t.pencolor('red')
t.speed(0)


def fun1():
    # 画左耳朵
    # t.fillcolor((254, 226, 90))
    # t.begin_fill()
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
    # t.end_fill()


fun1()

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

t.done()
