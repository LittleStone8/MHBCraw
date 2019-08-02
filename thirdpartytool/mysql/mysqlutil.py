# coding:utf-8
import time

import pymysql
from MySQLdb import cursors

from scheduler.threadpool import ThreadPool
from thirdpartytool.mysql import mysqlcommon
import MySQLdb
from DBUtils.PooledDB import PooledDB


class MysqlUtil:
    def __init__(self):
        self.mysqlhanndle = PooledDB(MySQLdb,maxconnections=mysqlcommon.mysql_link_pool_size,
            host=mysqlcommon.mysql_link_host,
            port=mysqlcommon.mysql_link_port,
            user=mysqlcommon.mysql_link_user,
            password=mysqlcommon.mysql_link_password,
            db=mysqlcommon.mysql_link_db,
            charset=mysqlcommon.mysql_link_charset,
            cursorclass = MySQLdb.cursors.DictCursor
            )
    pass

    def execute_commit(self,sql):
        conn = self.mysqlhanndle.connection()
        cur = conn.cursor()
        r = cur.execute(sql)
        cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return r
    pass

    def execute_query(self,sql):
        conn = self.mysqlhanndle.connection()
        cur = conn.cursor()
        cur.execute(sql)
        r = cur.fetchall()
        cur.close()
        conn.close()
        return r
    pass

mysqlutil=MysqlUtil()
def a():
    sql = "insert into x_server(area_id,name,xyq_id) values( '5', '5', '5')"
    #sql = "select * from x_server"
    print(mysqlutil.execute_commit(sql))
pass

def b():
    sql = "insert into x_server(area_id,name,xyq_id) values( '6', '6', '6')"
    #sql = "select * from x_server"
    mysqlutil.execute_commit(sql)
pass

def c():
    sql = "select * from x_server"
    #sql = "select * from x_server"
    print(mysqlutil.execute_query(sql))
pass

if __name__=="__main__":
    threadPool=ThreadPool(2)
    threadPool.run(b,())
    threadPool.run(a,())
    threadPool.run(c,())

''''
    mysqlUtil=MysqlUtil()
    #threadPool=ThreadPool(2)
    #threadPool.run()
    #sss=mysqlUtil.execute_no_commit('select * from x_server')
    sssw = mysqlUtil.execute_query('select * from x_server')
    sql = "insert into x_server(area_id,name,xyq_id) values( '2', '3', '4')"
    sss = mysqlUtil.execute_commit(sql)
    #for ss in sss:
    #    print(ss['id'])
    print(sssw)
    print(sss)
'''''