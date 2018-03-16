# coding:utf-8
import sys
import urllib
import re
reload(sys)
sys.setdefaultencoding('utf8')
import pyttsx
from coinmarketcap import Market
import json,sys,time
def speak(btc_price):
	engine = pyttsx.init()
	engine.say(btc_price)
	engine.runAndWait()
	#engine.endLoop()



def run():
	coinmarketcap = Market()
	l = 1

	jsonpack = coinmarketcap.ticker(limit=l, convert='CNY')



	for k in jsonpack:
	

		price =  k['name']+u'价格'+k['price_usd']+u'涨跌'+k['percent_change_24h']+'%'

		speak(price)

run()

while(True):
    try:
        run()
        time.sleep(60)
    except Exception, e:
        runerror =  str(e)
        print runerror
        time.sleep(60)
