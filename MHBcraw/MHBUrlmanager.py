# coding:utf-8
#
from MHBcraw.MHBcrawcommon import mhbcrawcommon
from MHBcraw.MHBcrawcommon.commonmap import cbg_MHB_request_url
from common.commonmap import MH_server_map
from common.server_info import server_info
from framemodule.UrlManager import UrlManager


class MHBUrlmanager(UrlManager):
    def __init__(self):
        self.page_start=mhbcrawcommon.mhbcraw_page_start
        self.page_end=mhbcrawcommon.mhbcraw_page_end
        self.cbg_MHB_request_url=cbg_MHB_request_url()
        pass

    def generate_cbg_MHB_request_url_by_parameter(self,server_ids,page_start,page_end):
        if len(server_ids)==0 or page_end<1:
            return
        cbg_MHB_request_urls=set()
        for server_id in server_ids:
            self.cbg_MHB_request_url.updata_server_id(server_id)
            for page in range(page_start,page_end+1):
                self.cbg_MHB_request_url.updata_page(page)
                cbg_MHB_request_urls.add(self.cbg_MHB_request_url.get_complete_url())
        self.new_urls=cbg_MHB_request_urls
        return cbg_MHB_request_urls
    pass

    def generate_cbg_MHB_request_quick(self):
        if len(MH_server_map.servers)==0 :
            return
        cbg_MHB_request_urls=set()
        for server in MH_server_map.servers:
            server_id=server.server_id
            self.cbg_MHB_request_url.updata_server_id(str(server_id))
            for page in range(self.page_start,self.page_end+1):
                self.cbg_MHB_request_url.updata_page(page)
                cbg_MHB_request_urls.add(self.cbg_MHB_request_url.get_complete_url())
        self.new_urls=cbg_MHB_request_urls
        return cbg_MHB_request_urls
    pass

    def generate_cbg_MHB_request_byserver(self,server):
        cbg_MHB_request_urls=set()
        server_id=server.server_id
        self.cbg_MHB_request_url.updata_server_id(str(server_id))
        for page in range(self.page_start,self.page_end+1):
            self.cbg_MHB_request_url.updata_page(page)
            cbg_MHB_request_urls.add(self.cbg_MHB_request_url.get_complete_url())
        return cbg_MHB_request_urls
    pass

# 主启动程序
if __name__=="__main__":
    urlManager = MHBUrlmanager()
    #server_ids=set()
    #server_ids.add(39)
    #server_ids.add(40)
    #urlManager.generate_cbg_MHB_request_quick()
    print (server_info)
