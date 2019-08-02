# coding=utf-8
from MHBcraw.MHBcrawcommon import mhbcrawcommon


class MHB_util:
    def generate_MHB_gold_trade_rediskey(self,server_id):
        return mhbcrawcommon.mhbcraw_gold_trade_rediskey_prefix+server_id
    pass

    def generate_MHB_last_gold_trade_rediskey(self,server_id):
        return mhbcrawcommon.mhbcraw_last_gold_trade_rediskey_prefix+server_id
    pass
mhb_util=MHB_util()