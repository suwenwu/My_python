import requests

import mysql


class Vegetable(object):
    __headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400"
    }
    __url = 'http://www.xinfadi.com.cn/getPriceData.html'

    __data = {
        "limit": '',
        "current": '',
        "pubDateStartTime": '',
        "pubDateEndTime": '',
        "prodPcatid": '',
        "prodCatid": '',
        "prodName": ''
    }

    __resp = None

    def __init__(self, limit, current):
        self.__data['limit'] = limit
        self.__data['current'] = current
        self.getResp()

    @classmethod
    def setCurrent(cls, current):
        cls.__data['current'] = current

    def getResp(self):
        self.__resp = requests.post(self.__url, headers=self.__headers, data=self.__data)
        return self.__resp

    def getData(self):
        dicts = self.__resp.json()
        sql = "insert into vegetable (prodName, lowPrice, highPrice, avgPrice, place, unitInfo, pubDate) values (%s,%s,%s,%s,%s,%s,%s) "
        db = mysql.DBUtil()
        for i in dicts['list']:
            if i['place'] == "":
                i['place'] = '未知地'
            data = (
                i['prodName'], float(i['lowPrice']), float(i['highPrice']),
                float(i['avgPrice']), i['place'], i['unitInfo'], i['pubDate']
            )
            # print(data)
            db.query(sql, data)

    def __del__(self):
        if self.__resp is not None:
            self.__resp.close()


def main():
    vege = Vegetable(20, 11)
    vege.getData()


def selectData():
    sql = "SELECT vegetable.prodName AS `菜名`,vegetable.lowPrice AS `最低价`," \
          "vegetable.highPrice AS `最高价`,vegetable.avgPrice AS `平均价`, " \
          "vegetable.place AS `产地`, vegetable.unitInfo AS `单位`, vegetable.pubDate AS `日期` " \
          "FROM vegetable"
    db = mysql.DBUtil()
    result = db.query(sql)
    for i in result:
        print(i)


if __name__ == '__main__':
    selectData()
