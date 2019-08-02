# coding=utf-8


#cbg MHB 请求方式url
import time

from common.url_parameter import url_parameter


class cbg_MHB_request_type:
    def __init__(self):
        self.Request_JSONP_request_map_request_0 = 0     # 名称
cbg_MHB_request_type = cbg_MHB_request_type() # 初始化结构对象

#cbg MHB 请求url
# https://recommd.xyq.cbg.163.com/cgi-bin/recommend.py?callback=Request.JSONP.request_map.request_0&_=1562818151825&act=recommd_by_role&server_id=39&areaid=33&server_name=%E4%B8%96%E7%95%8C%E4%B9%8B%E7%AA%97&page=2&kindid=23&view_loc=equip_list&count=15&order_by=unit_price%20ASC
# https://recommd.xyq.cbg.163.com/cgi-bin/recommend.py?
# callback=Request.JSONP.request_map.request_0&
# _=1562818151825&act=recommd_by_role&
# server_id=39&
# areaid=33&
# server_name=%E4%B8%96%E7%95%8C%E4%B9%8B%E7%AA%97&
# page=2&
# kindid=23&
# view_loc=equip_list&
# count=15&
# order_by=unit_price%20ASC
class cbg_MHB_request_url:
    def __init__(self):
        self.parameters = {}
        self.cbg_MHB_request_url = 'https://recommd.xyq.cbg.163.com/cgi-bin/recommend.py?'  # url
        self.parameters['callback']=(url_parameter('callback','Request.JSONP.request_map.request_0', 1))# 请求方式
        self.parameters['_']=(url_parameter('_', str(time.time()) , 1)) #时间
        self.parameters['act']=(url_parameter('act', 'recommd_by_role', 1)) # 角色推荐？？
        self.parameters['server_id']=(url_parameter('server_id', '39', 1)) # 服务器id  39应该对应是
        self.parameters['areaid']=(url_parameter('areaid', '33', 1)) # 服务大区 33应该对应是
        self.parameters['server_name']=(url_parameter('server_name', '%E4%B8%96%E7%95%8C%E4%B9%8B%E7%AA%97', 1)) #服务器名称
        self.parameters['page']=(url_parameter('page', '1', 1)) #页数
        self.parameters['kindid']=(url_parameter('kindid', '23', 1)) #查询的种类 23应该是MHB
        self.parameters['view_loc']=(url_parameter('view_loc', 'equip_list', 1)) #返回的实体数据类型？？
        self.parameters['count']=(url_parameter('count', '15', 1))  # 每页数据条数
        self.parameters['order_by']=(url_parameter('order_by', 'unit_price%20ASC', 1))  # 排序规则
    pass

    def get_complete_url(self):
        complete_url=self.cbg_MHB_request_url
        for parameter in self.parameters.values():
            if parameter.isnecessary==1:
                appstr=parameter.parameter+'='+parameter.value+'&'
                complete_url=complete_url+appstr
        return complete_url
    pass

    def updata_server_id(self,new_server_id):
        if self.parameters is None or new_server_id==0  or new_server_id is None:
            return
        server_id_parameter=self.parameters.get('server_id')
        server_id_parameter.value=str(new_server_id)
    pass

    def updata_page(self,new_page):
        if self.parameters is None or new_page==0  or new_page is None:
            return
        page_parameter=self.parameters.get('page')
        page_parameter.value=str(new_page)
    pass


# 主启动程序
if __name__=="__main__":
    asda=cbg_MHB_request_url()
    print (asda.get_complete_url())
    asda.updata_server_id(40)
    print (asda.get_complete_url())
    asda.updata_page(40)
    print (asda.get_complete_url())