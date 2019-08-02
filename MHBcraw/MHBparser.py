# coding:utf-8
import json
import re
import urllib.parse
from urllib.error import URLError

from bs4 import BeautifulSoup

from framemodule.Parser import Parser


class MHBparser(Parser):
    def __init__(self):
        self.p2 = re.compile(r'[(](.*)[)]', re.S)  # 取括号中的内容，贪婪取法
        pass

    # 解析mhb数据
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print ('parse_cbg_MHB_data 返回数据为空')
            return
        # html_cont 返回的数据为
        html_cont=str(html_cont)
        print(html_cont)
        try:
            www = re.findall(self.p2, html_cont)
        except URLError as e:
            print(e.reason)
            return
        jsonob = json.loads(www[0])
        status=jsonob.get('status')
        if status!=1:
            print('status error')
            return
        moneyinfolist = jsonob.get('equips')
        return moneyinfolist
        pass

