#爬取梨视频
import requests
from lxml import etree

#原网页
url = "https://www.pearvideo.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400"
}

resp = requests.get(url, headers=headers)
#将页面交给xpath解析
page_1 = etree.HTML(resp.text)
#查找所有视频的div
divs= page_1.xpath("//div[@class='ver-act-block pd040' or @class='ver-act-block pd040 padshow']")
url_1 = []
for div in divs:
    #查找所有a的href
    for i in div.xpath('.//a/@href'):
        #筛选video开头的href
        if(i.split("_")[0]=='video'):
            url_1.append(i)

for i in url_1:
    #拼接子页面的url
    url_son = url+i
    contId = i.split("_")[1]
    #设置视频url
    url3 = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.435357436857732"
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400",
        "Referer":  url_son
    }
    resp2 = requests.get(url3, headers=headers2)
    dics = resp2.json()
    #提取视频下载地址信息
    systemTime = dics["systemTime"];
    srcUrl = dics["videoInfo"]["videos"]["srcUrl"]
    resp3 = requests.get(url_son,headers=headers)
    name = etree.HTML(resp3.text).xpath("/html/head/title/text()")[0].split("-")[0]
    down_url = srcUrl.replace(systemTime,f"cont-{contId}")
    #下载视频
    with open("../video/"+down_url.split("/")[-1],mode="wb") as f:
        f.write(requests.get(down_url).content)


    print(name+"   下载完毕！")
    resp3.close()
    resp2.close()

resp.close()
