# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import csv

from scrapy_test.items import BittrexUsdtBtcItem

class ScrapyTestPipeline(object):
    def process_item(self, item, spider):
        return item

class BittrexUsdtBtcPipeline(object):
    def __init__(self):
        return

    def process_item(self,Item,spider):
        print('-----------------')
        data = [Item['Time'],Item['Open'],Item['High'],Item['Low'],Item['Close'],Item['Volume'],Item['BV']]
        print(data)
        with open('history.csv','a+',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        return Item


