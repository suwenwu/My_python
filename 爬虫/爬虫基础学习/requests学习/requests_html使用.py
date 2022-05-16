from requests_html import HTMLSession
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

session = HTMLSession()
url = 'http://news.youth.cn/'
# 随机请求头
ua = UserAgent().random
print(ua)
resp = session.get(url, headers={'user-agent': ua})
resp.encoding = resp.apparent_encoding

page = BeautifulSoup(resp.text, 'html.parser')
print(page.select('body > div.container > div.concent > div.mainL > div.topNew > div > div')[0].find('a').get('href'))
# print(page.find('a').text)
