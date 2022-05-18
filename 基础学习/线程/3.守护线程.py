import threading
import time

'''
    守护线程
    下面这个例子，这里使用setDaemon(True)把所有的子线程都变成了主线程的守护线程，
    因此当主线程结束后，子线程也会随之结束，所以当主线程结束后，整个程序就退出了。
    所谓’线程守护’，就是主线程不管该线程的执行情况，只要是其他子线程结束且主线程执行完毕，主线程都会关闭。也就是说:主线程不等待该守护线程的执行完再去关闭。
'''


def run(n):
    print('task', n)
    time.sleep(1)
    print('3s')
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')


if __name__ == '__main__':
    t = threading.Thread(target=run, args=('t1',))
    # 将 daemon 属性设为 True，必须在 start() 方法调用之前进行，否则会引发 RuntimeError 异常
    t.daemon = True
    t.start()
    # t.join()  # 设置join属性是为了让主线程等待子线程结束在执行
    print('end')
