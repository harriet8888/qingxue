#! /usr/bin/env python
#
# @brief XCoin API-call sample script (for Python 2.x, 3.x)
#
# @author btckorea
# @date 2017-04-14
#
# @details
# First, Build and install pycurl with the following commands::
# (if necessary, become root)
#
# https://pypi.python.org/pypi/pycurl/7.43.0#downloads
#
# tar xvfz pycurl-7.43.0.tar.gz
# cd pycurl-7.43.0
# python setup.py --libcurl-dll=libcurl.so install
# python setup.py --with-openssl install
# python setup.py install
#
# @note
# Make sure current system time is correct.
# If current system time is not correct, API request will not be processed normally.
#
# rdate -s time.nist.gov
#

import sys

from main.utils.httprequest import sendHttpGetRequest
from xcoin_api_client import *
import pprint


api_key = "api_connect_key"
api_secret = "api_secret_key"

api = XCoinAPI(api_key, api_secret)


#
# Public API
#
# /public/ticker
# /public/recent_ticker
# /public/orderbook
# /public/recent_transactions

def get_24h_closing_price():
	# result = api.xcoinApiCall("/public/ticker", rgParams)
	code, res_content = sendHttpGetRequest("https://api.bithumb.com/public/ticker/Qtum")
	print res_content
	result = json.loads(res_content)
	# print("Bithumb Public API URI('/public/ticker') Request...");
	# print("- Status Code: " + result["status"]);
	# print("- Opening Price: " + result["data"]["opening_price"]);
	print result
	krw = int(result["data"]["closing_price"])
	cny = float(krw * 0.0061)
	print("- Closing Price:%.2f "% cny)
	# print("- Sell Price: " + result["data"]["sell_price"]);
	# print("- Buy Price: " + result["data"]["buy_price"]);
	return cny,krw


rgParams = {
	# "order_currency" : "EOS",
	# "payment_currency" : "CNY"
}

def test():
	# result = api.xcoinApiCall("/public/ticker", rgParams)
	code, res_content = sendHttpGetRequest("https://api.bithumb.com/public/ticker",rgParams)
	print res_content
	# code, res_content = sendHttpGetRequest("https://api.bithumb.com/public/ticker/EOS")
	# result = json.loads(res_content)
	# print("Bithumb Public API URI('/public/ticker') Request...");
	# print("- Status Code: " + result["status"]);
	# print("- Opening Price: " + result["data"]["opening_price"]);
	# print("- Closing Price: " + result["data"]["closing_price"])
	# print("- Sell Price: " + result["data"]["sell_price"]);
	# print("- Buy Price: " + result["data"]["buy_price"]);

	# return result["data"]["closing_price"]



#
# Private API
#
# endpoint => parameters
# /info/current
# /info/account
# /info/balance
# /info/wallet_address

#print("Bithumb Private API URI('/info/account') Request...");
#result = api.xcoinApiCall("/info/account", rgParams);
#print("- Status Code: " + result["status"]);
#print("- Created: " + result["data"]["created"]);
#print("- Account ID: " + result["data"]["account_id"]);
#print("- Trade Fee: " + result["data"]["trade_fee"]);
#print("- Balance: " + result["data"]["balance"]);

#sys.exit(0)


if __name__ == '__main__':
	test()