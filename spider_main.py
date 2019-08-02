# coding:utf-8
import random
import time

from MHBcraw.MHBCraw import MHBCraw




# 主启动程序
from scheduler.myscheduler import Scheduler

if __name__=="__main__":
    scheduler = Scheduler()
    mHBCraw=MHBCraw(scheduler)
    scheduler.add_job(mHBCraw)
