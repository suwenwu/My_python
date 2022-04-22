import turtle as t
import random

for i in range(50):
    x = random.randint(-384, 384)
    y = random.randint(0, 512)
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(50, (r, g, b))
    t.right(90)
    t.pencolor((r, g, b))
    t.forward(80)
    t.left(90)
