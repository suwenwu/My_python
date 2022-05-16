import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "Host": "www.douban.com",
}
session = requests.Session()
resp = session.get('https://www.douban.com/', headers=headers)

print(resp.text)
