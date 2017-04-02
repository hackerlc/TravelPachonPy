# mysqldemo

import sys
import pymysql


class SQLManager:
    def __init__(self):
        self.addressName = "traver_address"
        try:
            self.conn = pymysql.connect(host="localhost",
                                       user="root", passwd="yichenziq1",
                                       db="traver", charset="utf8")
        except Exception:
            print("no")
            sys.exit()
        self.cursor = self.conn.cursor()

#关闭数据库
    def __delete__(self, instance):
        self.cursor.close()
        self.conn.close()

# 批量插入地点
    def setAddresses(self, addresses):
        sql = "INSERT INTO " + self.addressName + " (name) VALUES (%s)"
        for address in addresses:
            self.cursor.execute(sql, (address))
        self.conn.commit()

# 查询地点
    def getAddress(self, name=""):
        result = ""
        sql = "SELECT name FROM traver_address WHERE name like '%" + name + "'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.conn.commit()
        return result

# 删除库中文件自增id为0
    def deleteAddress(self):
        sql = 'TRUNCATE TABLE '+self.addressName
        self.cursor.execute(sql)
        self.conn.commit()
