# 地点爬虫
# 暂时确定爬取地点为马蜂窝

import sys
import os

# 按照层级把路径添加到sys.path中
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath = os.path.split(rootPath)[0]
rootPath = os.path.split(rootPath)[0]
sys.path.append(rootPath)

from TravelPachonPy.hub import URLHub
from TravelPachonPy.network import HttpHandler
from TravelPachonPy.network import HttpHandler
from TravelPachonPy.rehandler import AddressReHandler
from TravelPachonPy.sql import MySqlManager

html = HttpHandler.getHtml(URLHub.INIT_ADDRESS_URL)
# 获取到html后，根据筛选出地点名称
address = AddressReHandler.getAddress(html)

# 查询数据库中有没有数据并做区中操作，把新数据插入数据库中
sqlManager = MySqlManager.SQLManager()
oldData = sqlManager.getAddress()
print(oldData)
# 数据保存到数据库中
# sqlManager.setAddresses(address)
# 使用完毕
del sqlManager


