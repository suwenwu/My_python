import asyncio
import aiohttp
import aiofiles

urls = [
    'http://img.sccnn.com/bimg/340/03387.jpg',
    'http://img.sccnn.com/bimg/340/03384.jpg',
    'http://img.sccnn.com/bimg/340/03381.jpg'
]


async def download(url):
    name = url.rsplit('/', 1)[-1]
    async with aiohttp.ClientSession() as session:  # 相当于requests.session
        async with session.get(url) as resp:
            # 异步读取文件aiofiles
            async with aiofiles.open(f'../img/{name}', mode='wb') as f:
                await f.write(await resp.content.read())

    print(name, '下载完毕')


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
