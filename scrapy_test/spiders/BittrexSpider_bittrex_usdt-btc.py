# -*- coding: utf-8 -*-

import scrapy
import json
import time

from scrapy_test.items import BittrexUsdtBtcItem

class Bittrex_usdt_btc(scrapy.Spider):
    name = 'bittrex-usdt-btc'
    allowed_domains = ['bittrex.com']
    start_urls = ['https://bittrex.com/Api/v2.0/pub/market/GetLatestTick?marketName=USDT-BTC&tickInterval=oneMin']
    connection = None

    def parse(self,response):
        if response.status == 200:
            response = json.loads(response.body.decode('utf-8'))
            for i in response['result']:
                item = BittrexUsdtBtcItem()
                item['Time'] = i['T']
                item['Open'] = i['O']
                item['High'] = i['H']
                item['Low'] = i['L']
                item['Close'] = i['C']
                item['Volume'] = i['V']
                item['BV'] = i['BV']
                yield item

