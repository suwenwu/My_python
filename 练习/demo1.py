from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(10000):
            print(self.name, i)


if __name__ == '__main__':
    t = MyThread('小黑')
    t.start()
    for i in range(10000):
        print('主线程:', i)
