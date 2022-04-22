import turtle as t
import pygame
import time

pygame.mixer.init()

track = pygame.mixer.music.load('../bgm/bg1.mp3')

pygame.mixer.music.play()

# 设置窗口标题
t.title('元宵节快乐')
# 设置窗口大小1000*745
t.setup(1000, 745)
# 设置窗口图片
t.bgpic('img/img.png')
# 设置画笔颜色和填充颜色
t.color('black', 'black')
# 隐藏画笔
t.hideturtle()

# 中间元宵
t.penup()
t.goto(-280, 100)
t.pendown()
t.write('~^o^~', font=('Arial', 25, 'normal'))

time.sleep(0.5)

# 第二个元宵
t.penup()
t.goto(-375, 40)
t.pendown()
t.write('(っ◔◡◔)っ ♥', font=('Arial', 15, 'bold'))

time.sleep(0.5)
# 第三个元宵
t.penup()
t.goto(-250, 30)
t.pendown()
t.write('♥(ˆ⌣ˆԅ)', font=('Arial', 15, 'bold'))
time.sleep(0.5)
# 第四个元宵
t.penup()
t.goto(-180, 90)
t.pendown()
t.write('(◑‿◑)', font=('Arial', 25, 'normal'))
time.sleep(0.5)
# 第五个元宵
t.penup()
t.goto(-210, 155)
t.pendown()
t.write('(¬‿¬)', font=('Arial', 25, 'normal'))
time.sleep(0.5)
# 第六个元宵
t.penup()
t.goto(-290, 180)
t.pendown()
t.write('(ô‿ô)', font=('Arial', 25, 'normal'))
time.sleep(0.5)
# 第七个元宵
t.penup()
t.goto(-370, 130)
t.pendown()
t.write('(◑‿◑)', font=('Arial', 25, 'normal'))

t.done()
