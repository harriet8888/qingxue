# encoding: utf-8

'''
@author: renhong
@time: 2018/1/7 11:31
'''
from main.utils.redisutil import Cache
from main.monitor.constant import *


class Threshold():
    cache = Cache()

    def get_lowprice(self):
        low_price = int(self.cache.get(low_price_key))
        return low_price

    def get_highprice(self):
        high_price = int(self.cache.get(high_price_key))
        return high_price

    def set_lowprice(self, low_price):
        self.cache.set(low_price_key, low_price, -1)

    def set_highprice(self, high_price):
        self.cache.set(low_price_key, high_price, -1)

    def get_alarm_times(self):
        value = self.cache.get(alarm_times)
        if value:
            return int(value)
        else:
            return 0