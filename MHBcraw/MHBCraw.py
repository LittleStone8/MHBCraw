import random
import time

from MHBcraw.MHBUrlmanager import MHBUrlmanager
from MHBcraw.MHBdownloader import MHBdownloader
from MHBcraw.MHBoutputer import MHBoutputer
from MHBcraw.MHBparser import MHBparser
from common.commonmap import MH_server_map
from framemodule.Craw import Craw


class MHBCraw(Craw):
    def __init__(self,Scheduler):
        self.urlmanager = MHBUrlmanager()
        self.downloader = MHBdownloader()
        self.parser = MHBparser()
        self.outputer = MHBoutputer()
        self.scheduler = Scheduler
        self.job_interval = 500
        pass
    def docraw(self):
        self.start_craw()
        if self.job_interval!=0:
            self.scheduler.timer.addtask(self.start_craw,self.job_interval)
        pass

    def start_craw(self):
        print('启动开始抓取cbg_MHB任务:')
        servers=MH_server_map.servers
        for server in servers:
            for url in self.urlmanager.generate_cbg_MHB_request_byserver(server):
                self.scheduler.run_in_main_threadpool(func=self.craw, args=(url,))
    pass

    def craw(self,url):
        print('开始抓取:'+url)
        html = self.downloader.download_by_myself_useagent(url)
        moneyInfoData = self.parser.parse(url, html)
        self.outputer.collect_data_to_print(moneyInfoData)

        #print(url + "抓取完毕,入库:"+str(storagesum))
