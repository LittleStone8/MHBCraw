# coding:utf-8
import configparser
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("pythonspace\\")+len("pythonspace\\")]  # 获取myProject，也就是项目的根路径
conf = configparser.ConfigParser()
conf.read(rootPath+'\\cofig.ini')


class mhbcrawcommon:
    def __init__(self):
        self.mhbcraw_max_quest_timeout = conf.getint('MHBCraw', 'mhbcraw_max_quest_timeout')
        self.mhbcraw_page_start= conf.getint('MHBCraw', 'mhbcraw_page_start')
        self.mhbcraw_page_end = conf.getint('MHBCraw', 'mhbcraw_page_end')
        self.mhbcraw_gold_trade_rediskey_prefix='cbg_mhbcraw_gold_trade_'
        self.mhbcraw_last_gold_trade_rediskey_prefix = 'cbg_mhbcraw_last_gold_trade_'
    pass

mhbcrawcommonObject=mhbcrawcommon()
mhbcraw_max_quest_timeout = mhbcrawcommonObject.mhbcraw_max_quest_timeout
mhbcraw_page_start= mhbcrawcommonObject.mhbcraw_page_start
mhbcraw_page_end=mhbcrawcommonObject.mhbcraw_page_end
mhbcraw_gold_trade_rediskey_prefix=mhbcrawcommonObject.mhbcraw_gold_trade_rediskey_prefix
mhbcraw_last_gold_trade_rediskey_prefix=mhbcrawcommonObject.mhbcraw_last_gold_trade_rediskey_prefix




