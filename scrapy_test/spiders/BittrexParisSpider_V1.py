# -*- coding: utf-8 -*-

import scrapy
import json

from scrapy_test.items import BittrexParisV1Item

class BittrexParisV1Spider(scrapy.Spider):
    name = 'bittrex-paris-v1'
    allowed_domains = ['bittrex.com']
    start_urls = ['https://bittrex.com/api/v1.1/public/getmarkets']
    connection = None

    def parse(self,response):
        if response.status == 200:
            response = json.loads(response.body.decode('utf-8'))
            for i in response['result']:
                item = BittrexParisV1Item()
                item['Market_Currency'] = i['MarketCurrency']
                item['Base_currency'] = i['BaseCurrency']
                item['Market_CurrencyLong'] = i['MarketCurrencyLong']
                item['Base_CurrencyLong'] = i['BaseCurrencyLong']
                yield item

