#-*-coding:utf-8-*-
'''
Created on 2017年5月13日

@author: xiabing
'''
import json
import urllib2
import urllib


def sendHttpPostRequest(url,data=None,headers=None):
    '''
        send a http post request
        headers sample: {'Content-Type' : 'application/json'}
    '''
    try:
        req = None
        if data:
            if headers:
                req = urllib2.Request(url, data, headers)
            else:
                req = urllib2.Request(url, data)
        res = urllib2.urlopen(req)
        code = res.getcode()
        res_content = res.read()
        res.close()
        # print res_content
        return code, res_content
    except urllib2.HTTPError, e:
        return e.code, None

def sendHttpPostRequest_res(url,data=None,headers=None):
    '''
        send a http post request
        headers sample: {'Content-Type' : 'application/json'}
    '''
    try:
        req = None
        if data:
            if headers:
                req = urllib2.Request(url, data, headers)
            else:
                req = urllib2.Request(url, data)
        res = urllib2.urlopen(req)
        code = res.getcode()
        res_content = res.read()
        res.close()
        # print res_content
        return res,res_content,code
    except urllib2.HTTPError, e:
        return None, None,e.code

def sendHttpGetRequest(url, params=None, headers=None):
    '''
        send a http get request
    '''
    req = None
    if params:
        params = urllib.urlencode(params)
        url = "%s?%s"%(url, params)
    if headers:
        req = urllib2.Request(url, headers)
    else:
        req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    code = res.getcode()
    res_content = res.read()
    res.close()
    return code, res_content
    


if __name__ == '__main__':
    print sendHttpGetRequest('http://www.baidu.com')
