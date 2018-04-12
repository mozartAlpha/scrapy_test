# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BittrexPairsItem(scrapy.Item):
    base_currency = scrapy.Field()
    quote_currency = scrapy.Field()
    base_currency_name = scrapy.Field()
    quote_currency_name = scrapy.Field()

class BittrexUsdtBtcItem(scrapy.Item):
    Time = scrapy.Field()
    Open = scrapy.Field()
    High = scrapy.Field()
    Low = scrapy.Field()
    Close = scrapy.Field()
    Volume = scrapy.Field()
    BV = scrapy.Field()


