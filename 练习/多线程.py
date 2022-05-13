from threading import Thread
import turtle


def draw1():
    pen1 = turtle.Pen()
    pen1.forward(30)


def draw2():
    pen2 = turtle.Pen()
    pen2.backward(30)


if __name__ == '__main__':
    t1 = Thread(target=draw1)
    t2 = Thread(target=draw2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("执行结束")
