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

class BittrexParisV1Item(scrapy.Item):
    Market_Currency = scrapy.Field()
    Base_currency = scrapy.Field()
    Market_CurrencyLong = scrapy.Field()
    Base_CurrencyLong = scrapy.Field()

class BittrexUsdtBtcItem(scrapy.Item):
    Time = scrapy.Field()
    Open = scrapy.Field()
    High = scrapy.Field()
    Low = scrapy.Field()
    Close = scrapy.Field()
    Volume = scrapy.Field()
    BV = scrapy.Field()


