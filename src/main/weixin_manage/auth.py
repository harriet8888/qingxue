# encoding: utf-8

'''
@author: renhong
@time: 2018/1/6 08:45
'''
import json

from src.main.utils.httprequest import sendHttpGetRequest

# Secret = "gr5tnqlYKjNo2ZqlskZ69d2Er8oxGHOSIMEoQqVhTS8"

CorpID = "ww86dc7419d9b290c5"
qingxue_Secret = "gr5tnqlYKjNo2ZqlskZ69d2Er8oxGHOSIMEoQqVhTS8"
ACCESS_API = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s"


class WeiXinPublic():
    @classmethod
    def get_accesstoken(self):
        code, result = sendHttpGetRequest(ACCESS_API % (CorpID, qingxue_Secret))
        result_json = json.loads(result)
        if (result_json['errcode'] == 0):
            return result_json['access_token'], result_json['expires_in']
        else:
            return "", 0


if __name__ == '__main__':
    print WeiXinPublic.get_accesstoken()
