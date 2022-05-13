# 1. 导入画图工具库和随机库
import turtle
import random as ra
from threading import Thread

# 2. 隐藏画笔，速度设为最快，画笔的大小设置为3，颜色设置为红色

turtle.ht()
turtle.speed(0)
turtle.pensize(3)
turtle.pencolor('red')
# 3. 关闭乌龟轨迹
turtle.tracer(0)


def draw_love():
    t1 = turtle.Pen()
    # 4. 循环150次
    for i in range(150):
        # 5. 清屏
        t1.clear()
        # 6. 提笔，走到（0，-400+i*3），落笔
        t1.penup()
        t1.goto(0, -400 + i * 3)
        t1.pendown()
        # 7. 填充三剑客，设置填充颜色，开始填充
        t1.fillcolor('pink')
        t1.begin_fill()
        # 8. 先画左半边爱心轮廓
        t1.seth(135)
        t1.forward(150)
        t1.circle(-75, 180)
        # 9. 再画右半边爱心轮廓
        t1.seth(45)
        t1.circle(-75, 180)
        t1.forward(150)
        # 10. 结束填充
        t1.end_fill()
        # 11. 提笔，向上直行150
        t1.penup()
        t1.seth(90)
        t1.forward(150)
        # 12. 设置填充颜色白色
        t1.fillcolor('white')
        # 13. 写出内容“母亲节快乐”，居中，字体“楷体”，33号，加粗
        t1.write("母亲节快乐", align="center", font=("Arial", 33, "bold"))
        # 14. 更新到屏幕上
        t1.update()


def draw_wishes():
    t2 = turtle.Pen()
    # 15.列表name
    name = ["妈妈，", "母亲，", 'mom，']
    # 16.祝福语列表
    wishes = ['❤', '辛苦啦!', '向你比心', '出去散散步', '母亲节快乐！', '永远在一起!', '你是100分妈妈！']
    # 17.循环出现35个祝福
    for i in range(35):
        # 18. 横坐标x是（-330,350）之间的随机数
        #    纵坐标是（-500,500）之间的随机数
        x = ra.randint(-330, 350)
        y = ra.randint(-500, 500)
        # 19. r,g,b是(0.4,1)之间的随机小数
        r = ra.uniform(0.4, 1)
        g = ra.uniform(0.4, 1)
        b = ra.uniform(0.4, 1)
        # 20. 提笔走到（x,y）处
        t2.penup()
        t2.goto(x, y)
        # 21. 随机生成祝福语文本
        text = ra.choice(name) + ra.choice(wishes)
        # 22. 填充颜色随机（r,g,b）
        t2.fillcolor(r, g, b)
        # 23. 写出随机祝福语
        t2.write(text, align="center", font=("Arial", ra.randint(10, 40), 'bold'))
        # 24. 更新到屏幕上
        t2.update()


if __name__ == '__main__':
    threads = []
    th1 = Thread(target=draw_love)
    threads.append(th1)
    th2 = Thread(target=draw_wishes)
    threads.append(th2)

    for i in threads:
        i.start()
    for i in threads:
        i.join()
    turtle.mainloop()
