import re

import requests
from bs4 import BeautifulSoup


url = "https://www.cccsc.cn/index.php?app=search&cate_id=5"

resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

'''bs4解析
#解析数据，讲页面源代码交给bs4处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")#指定html解析

#从bs对象查找数据find(标签，属性) 和 find_all(标签，属性)
# table = page.find_all("a", target="_blank")
divs = page.find_all("div", attrs={"class": "content"})
# h2s = page.find_all('h2')
# for h2 in h2s:
#     name = h2.text
#     print(name)

# print(divs[1])
names = divs[1].find_all('h2')
prices = divs[1].find_all('div', attrs={"class": 'p-price'})
for i in range(len(names)):
    print(names[i].text, prices[i].text)


resp.close()
'''

#正则解析

obj = re.compile(r'<h2><a href=".*?" target="_blank">(?P<name>.*?)</a></h2>'
                 r'.*?商城价：<span>(?P<price>.*?)</span></div>', re.S)

result = obj.finditer(resp.text)
for i in result:
    print(i.group('name'), i.group('price'))

resp.close()