'''
递归锁是同步锁的一个升级版本，在同步锁的基础上可以做到连续重复使用多次acquire()后
再重复使用多次release()的操作，但是一定要注意加锁次数和解锁次数必须一致，否则也将引发死锁现象。
'''

from threading import Thread, RLock


def fun1():
    global n

    for i in range(1000):
        lock.acquire()
        lock.acquire()
        n += 1
        lock.release()
        lock.release()
        print(f"fun1里n的值是：{n}")


def fun2():
    global n
    with lock:
        for i in range(1000):
            n += 1
            print(f"fun2里n的值是：{n}")


if __name__ == '__main__':
    n = 0
    lock = RLock()
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
