# coding:utf-8
import time
import urllib.request
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

from MHBcraw.MHBcrawcommon import mhbcrawcommon
from agentpool.agentmanager import agentmanagerutil, agentmanagercommon
from common.httpheader import getheaders
from framemodule.Downloader import Downloader


class MHBdownloader(Downloader):
    def download_by_myself(self, url):
        return self.download_by_father(self, url)

    def download_by_myself_useagent(self, url):
        proxiesips=agentmanagerutil.agentmanagerutil.providing_quality_proxie()
        for proxiesipstr in proxiesips:
            if proxiesips ==None:
                continue
            else:
                headers = getheaders()  # 定制请求头
                proxies = {"http": "http://" + proxiesipstr, "https": "http://" + proxiesipstr}  # 代理ip
                agentmanagercommon.agentmanager_requestsum = agentmanagercommon.agentmanager_requestsum + 1
                agentmanagercommon.agentmanager_use_proxy_time = agentmanagercommon.agentmanager_use_proxy_time + 1
                response = self.download_by_father_useagent(url, headers, mhbcrawcommon.mhbcraw_max_quest_timeout, proxies)
                if response is None:
                    agentmanagerutil.agentmanagerutil.use_updates_proxie(proxiesipstr,False)
                else:
                    agentmanagerutil.agentmanagerutil.use_updates_proxie(proxiesipstr,True)
                    agentmanagercommon.agentmanager_use_proxy_success_time = agentmanagercommon.agentmanager_use_proxy_success_time + 1
                    return response
            time.sleep(0.1)
        return self.download_by_myself(url)
    pass