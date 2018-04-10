# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy_test.items import BittrexPairsItem


class BinancePairsSpider(scrapy.Spider):
    name = 'bittrex-pairs'
    allowed_domains = ['bittrex.com']
    start_urls = ['https://bittrex.com/api/v2.0/pub/Markets/GetMarketSummaries']
    connection = None

    def parse(self, response):
        if response.status == 200:
            response = json.loads(response.body.decode('utf-8'))
            for i in response['result']:
                item = BittrexPairsItem()
                item['base_currency'] = i['Market']['BaseCurrency']
                item['quote_currency'] = i['Market']['MarketCurrency']
                item['base_currency_name'] = i['Market']['BaseCurrencyLong']
                item['quote_currency_name'] = i['Market']['MarketCurrencyLong']
                yield item

