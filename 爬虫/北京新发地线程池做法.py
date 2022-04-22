import requests
import csv
from concurrent.futures import ThreadPoolExecutor
url = 'http://www.xinfadi.com.cn/getPriceData.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400"
}
data = {
    "limit": '',
    "current": '',
    "pubDateStartTime": '',
    "pubDateEndTime": '',
    "prodPcatid": '',
    "prodCatid": '',
    "prodName": ''
}

f = open('../other/新发地菜价.csv',mode='w',encoding='utf-8')
csvwrite = csv.writer(f)
def download_one(data):
    resp = requests.post(url,headers=headers,data=data)
    dics = resp.json()
    info = {}
    j = 1
    for i in dics['list']:
        c = {}
        c['菜名'] = i['prodName']
        c['最低价'] = i['lowPrice']
        c['最高价'] = i['highPrice']
        c['平均价'] = i['avgPrice']
        c['产地'] = i['place']
        c['单位'] = i['unitInfo']
        c['发布时间'] = i['pubDate']
        info[j] = c
        j+=1
    print(info)
    for i in info:
        csvwrite.writerow(info[i].values())
    resp.close()
    print("")


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        download_one(data)
        for i in range(1,20):
            try:
                data['limit'] = str(20)
                data['current'] = str(i)
                download_one(data)
            except:
                print("跳过")
    f.close()
    print('下载完毕')
