import pymysql


# mysql数据库类
class DBUtil(object):
    __db = None
    __config = {
        'host': "localhost",
        'port': 3306,
        'user': "root",
        'password': 'root',
        'db': "python",
        'charset': "utf8"
    }

    def __connect(self):
        if self.__db is None:
            self.__db = pymysql.Connect(
                host=self.__config['host'],
                port=self.__config['port'],
                user=self.__config['user'],
                passwd=self.__config['password'],
                db=self.__config['db'],
                charset=self.__config['charset']
            )
        return self.__db

    def __init__(self):
        self.__connect()

    def query(self, sql, args=None):
        __cursor = self.__db.cursor()
        try:
            __cursor.execute(sql, args)
            result = __cursor.fetchall()
            self.__db.commit()
        except:
            self.__db.rollback()
            print("提交错误")
            return False
        return result

    def __del__(self):
        if self.__db is not None:
            self.__db.close()


def main():
    db = DBUtil()
    # sql = 'insert into vegetable (prodName,lowPrice,highPrice,avgPrice,place,unitInfo,pubDate) values (%s,%s,%s,%s,%s,%s,%s) '
    # data = ('小青菜', 1.68, 2.1, 2.0, '南京', '斤', '2022-4-21')
    # sql = 'update vegetable set prodName=%s,lowPrice=%s,highPrice=%s,avgPrice=%s where id = 2'
    # data = ('蒜苔', 8.2, 9.3, 9.0)
    sql = 'select * from vegetable'
    result = db.query(sql)
    print(result)


def selectAll():
    pass


if __name__ == '__main__':
    main()
