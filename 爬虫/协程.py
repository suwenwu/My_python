import asyncio


# async def fun1():
#     print('我叫李雪琴！')
#     await asyncio.sleep(2)
#     print('我叫李雪琴！')
#
#
# async def fun2():
#     print('我叫杨笠！')
#     await asyncio.sleep(3)
#     print('我叫杨笠！')
#
#
# async def fun3():
#     print('我叫何广智！')
#     await asyncio.sleep(4)
#     print('我叫何广智！')
#
#
# async def main():
#     tasks = [
#         fun1(),
#         fun2(),
#         fun3()
#     ]
#     await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


async def download(url):
    print('开始下载！')
    await asyncio.sleep(2)
    print('结束下载！')


async def main():
    urls = [
        'www.baidu.com',
        'www.4399.com',
        'www.qq.com'
    ]
    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(asyncio.create_task(d))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
