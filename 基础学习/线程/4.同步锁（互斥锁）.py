from threading import Thread, Lock

'''
def fun1():
    global n
    for i in range(1000000):
        n += 1
    print(f"fun1里n的值是：{n}")


def fun2():
    global n
    for i in range(1000000):
        n += 1
    print(f"fun2里n的值是：{n}")


if __name__ == '__main__':
    n = 0
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
'''

'''
    由于线程之间是进行随机调度，并且每个线程可能只执行n条执行之后，
    当多个线程同时修改同一条数据时可能会出现脏数据，
    所以出现了线程锁，即同一时刻允许一个线程执行操作。
    线程锁用于锁定资源，可以定义多个锁，像下面的代码，当需要独占某一个资源时，
    任何一个锁都可以锁定这个资源，就好比你用不同的锁都可以把这个相同的门锁住一样。
        由于线程之间是进行随机调度的，如果有多个线程同时操作一个对象，如果没有很好地保护该对象，
    会造成程序结果的不可预期，我们因此也称为“线程不安全”。
        为了防止上面情况的发生，就出现了互斥锁（Lock）

'''

'''
互斥锁只可以出现一个锁，如果出现多个锁，会出现死锁的情况
'''


def fun1():
    global n

    for i in range(1000):
        lock.acquire()
        n += 1
        lock.release()
        print(f"fun1里n的值是：{n}")


def fun2():
    global n

    for i in range(1000):
        lock.acquire()
        n += 1
        lock.release()
        print(f"fun2里n的值是：{n}")


if __name__ == '__main__':
    n = 0
    lock = Lock()
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
