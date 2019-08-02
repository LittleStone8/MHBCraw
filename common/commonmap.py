# coding=utf-8

#cbg MHB 请求方式
import time

from common.server_info import server_info


#MH对应服务器
class MH_server_map:
    def __init__(self):
        self.servers = set()
        self.servers.add(server_info('39', 'xxx','32', 'xxx'))  #
    pass
MH_server_map = MH_server_map() # 初始化结构对象


