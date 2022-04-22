from concurrent.futures import ThreadPoolExecutor

def fun(name):
    for i in range(100):
        print(f"线程{name} {i}")

if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fun,name=i)
    print("over")