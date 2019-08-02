# coding:utf-8
import configparser
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("pythonspace\\")+len("pythonspace\\")]  # 获取myProject，也就是项目的根路径
conf = configparser.ConfigParser()
conf.read(rootPath+'\\cofig.ini')


class MysqlCommon:
    def __init__(self):
        self.host = conf.get('mysql', 'host')
        self.port = conf.getint('mysql', 'port')
        self.user = conf.get('mysql', 'user')
        self.password = conf.get('mysql', 'password')
        self.db = conf.get('mysql', 'db')
        self.charset = conf.get('mysql', 'charset')
        self.pool_size = conf.getint('mysql', 'pool_size')
    pass
mysqlcommonObject=MysqlCommon()
mysql_link_host = mysqlcommonObject.host
mysql_link_port = mysqlcommonObject.port
mysql_link_user = mysqlcommonObject.user
mysql_link_password = mysqlcommonObject.password
mysql_link_db =mysqlcommonObject.db
mysql_link_charset = mysqlcommonObject.charset
mysql_link_pool_size= mysqlcommonObject.pool_size