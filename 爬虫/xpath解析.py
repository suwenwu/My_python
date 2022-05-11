"""
通过节点进行修饰
/html/body/div
/html/body/div[3]
/html/body/div[last()]
/html/body/div[last()-1]
/html/body/div[position()>=10] 范围选择，位置大于等于10的

通过属性值修饰
//div[@id='content'] 

通过节点进行修饰
//div[i>2000]

通过包含进行修饰
//div[contains(@id,'qishi_tag_')] 包含属性相同元素的都会被选择
//div[contains(text(),'下一页')] 包含元素相同元素的都会被选择

获取属性值
//img/@href

获取文本值
//span/text()
"""
import requests
from lxml import etree


class Tieba(object):

    def __init__(self, name):
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(name)
        # print(self.url)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
        }

    def get_resp(self, url):
        resp = requests.get(url, self.headers)
        return resp.content

    def parse_data(self, data):
        data = data.decode()
        html = etree.HTML(data)
        a_list = html.xpath('//li/div/div[2]/div[1]/div[1]/a')
        data_list = []
        for a in a_list:
            temp = {}
            temp['title'] = a.xpath('./text()')[0]
            temp['link'] = 'http://tieba.baidu.com' + a.xpath('./@href')[0]
            data_list.append(temp)
        # 获取下一页url
        try:
            next_url = 'https:' + html.xpath("//a[contains(text(),'下一页')]/@href")[0]
        except:
            next_url = None
        return data_list, next_url

    def print_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        next_url = self.url
        while True:
            data = self.get_resp(next_url)
            data_list, next_url = self.parse_data(data)
            self.print_data(data_list)
            print(next_url)
            if next_url is None:
                break


if __name__ == '__main__':
    tieba = Tieba('剑灵')
    tieba.run()
