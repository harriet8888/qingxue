# encoding: utf-8

'''
@author: renhong
@time: 2018/1/6 10:46
'''
import time

from main.monitor.real_time_status import get_24h_closing_price
from main.monitor.threshold_dao import Threshold
from main.utils.redisutil import Cache
from main.weixin_manage.message import *
from main.monitor.constant import *
import traceback


# LOW_PRICE = "22035000"
# HIGH_PRICE = "28035000"



class Monitor():
    cache = Cache()
    threshold = Threshold()

    @classmethod
    def check_price(self):
        while True:
            try:
                time.sleep(1)
                cny, krw = get_24h_closing_price()
                low_price = self.threshold.get_lowprice()
                high_price = self.threshold.get_highprice()
                if cny < low_price:
                    if self.cache.haskey(alarming) == False and self.threshold.get_alarm_times() < 5 or self.cache.get(
                            alarm_times) == None :
                        str = "跌！！主人，实时价格跌破了最低阈值(%d)，当前：CNY:%.2f，KRW:%d" % (low_price, cny, krw)
                        Message.send_message(str)
                        self.cache.set(alarming, 1, 60)
                        if self.cache.get(alarm_times) == None:
                            self.cache.set(alarm_times, 1, 1800)
                        else:
                            self.cache.incr(alarm_times)

                if cny > high_price:
                    if self.cache.haskey(alarming) == False and self.threshold.get_alarm_times() < 5 or self.cache.get(
                            alarm_times) == None:
                        str = "涨！！主人，实时价格飞过了最高阈值(%d)，当前：CNY:%.2f，KRW:%d" % (high_price, cny, krw)
                        Message.send_message(str)
                        self.cache.set(alarming, 1, 60)
                        if self.cache.get(alarm_times) == None:
                            self.cache.set(alarm_times, 1, 1800)
                        else:
                            self.cache.incr(alarm_times)
            except:
                traceback.print_exc()


if __name__ == '__main__':
    Monitor.check_price()
    # mon = Monitor()
    # print type(mon.cache.get(alarm_times))
