# coding:utf-8
from MHBcraw.MHBcrawcommon.util import mhb_util
from MHBcraw.bean.gold_trade import gold_trade
from framemodule.Outputer import Outputer


class MHBoutputer(Outputer):
    def __init__(self):
        self.gold_trade=gold_trade()
        pass

    def collect_data_to_mysql(self, data):
        pass

    def collect_data_to_redis(self, data):
        pass

    def collect_data_to_print(self, datas):
        for data in datas:
            eid=data['eid']
            server_id = data['server_id']
            mhb_util.generate_MHB_gold_trade_rediskey(server_id)
            mhb_util.generate_MHB_last_gold_trade_rediskey(server_id)

        pass


