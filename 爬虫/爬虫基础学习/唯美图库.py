import requests
from bs4 import BeautifulSoup
import time

url = 'http://www.sccnn.com/gaojingtuku/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400"
}

resp = requests.get(url, headers=headers)
resp.encoding = 'Gb2312' #处理乱码

main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find('tbody').find_all('a', target="_blank")
k = True
for i in alist:
    if k:
        url2 = "http://www.sccnn.com"
        child_url = url2+i.get('href')
        child_resp = requests.get(child_url, headers=headers)
        child_resp.encoding = 'Gb2312'
        child_page = BeautifulSoup(child_resp.text, "html.parser")
        src = child_page.find('div', class_="PhotoDiv").find('img').get('src')
        img_resp = requests.get(src)
        img_name = src.split('/')[-1]
        with open("../image/"+img_name, mode='wb') as f:
            f.write(img_resp.content)
        print(img_name, "下载完毕")


        img_resp.close()
        child_resp.close()
        time.sleep(1)
    k = bool(1-k)


print("全部下载完毕！")
resp.close()