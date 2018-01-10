# encoding: utf-8

'''
@author: renhong
@time: 2018/1/6 22:22
'''

import redis


class Cache():
    con = None

    def __init__(self):
        self.con = redis.Redis(host='127.0.0.1', port=6379, db=0)

    def get(self, key):
        return self.con.get(key)

    def haskey(self, key):
        value = self.con.get(key)
        if value:
            return True
        else:
            return False

    def set(self, key, value, expire):
        self.con.set(key, value, expire)

    def incr(self, key):
        self.con.incr(key)


if __name__ == '__main__':
    cache = Cache()
    print cache.haskey("alaming")
    print cache.get("alamtimes")
    print cache.get("alamtimes")
    print cache.set("alaming", 1, 60)
    print cache.incr("alamtimes")

