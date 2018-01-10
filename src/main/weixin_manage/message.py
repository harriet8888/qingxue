# encoding: utf-8

'''
@author: renhong
@time: 2018/1/6 08:45
'''
import json

from main.utils.httprequest import sendHttpPostRequest
from main.utils.redisutil import Cache
from main.weixin_manage.auth import WeiXinPublic
from main.monitor.constant import *

AgentId = 1000002
WEIXINSEND = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s"

message_body = {
    "touser": "",
    "toparty": "1",
    "totag": "",
    "msgtype": "text",
    "agentid": AgentId,
    "text": {
        "content": "%s"
    },
    "safe": 0
}


class Message:
    cache = Cache()

    @classmethod
    def send_message(self, message):
        if self.cache.haskey(access_token):
            token = self.cache.get(access_token)
        else:
            token, expire = WeiXinPublic.get_accesstoken()
            self.cache.set(key=access_token, value=token, expire=expire)
        url = WEIXINSEND % token
        message_body['text']['content'] = message
        request_body = message_body
        code, res_content = sendHttpPostRequest(url, json.dumps(request_body))
        print res_content


if __name__ == '__main__':
    Message.send_message("develop test")
