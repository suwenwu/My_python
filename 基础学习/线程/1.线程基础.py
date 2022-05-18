import time
from threading import Thread


def run(n):
    print(f'子线程{n}开始')
    time.sleep(2)
    print(f'子线程{n}结束')


if __name__ == '__main__':
    print('主线程开始')
    t1 = Thread(target=run, args=(1,))
    t2 = Thread(target=run, args=(2,))
    t1.start()
    t2.start()
    print('主线程结束')
