from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self, name=name)
        self.name = name

    def run(self):
        for i in range(10):
            print(f'线程{self.name}执行第{i}次')
        print(f'线程{self.name}执行结束')


if __name__ == '__main__':
    t1 = MyThread(name='t1')
    t2 = MyThread(name='t2')
    t1.start()
    t2.start()
    print('主线程结束')
