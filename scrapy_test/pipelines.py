# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


##import csv
import psycopg2

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
        print(type(data))
        print('' + Item['Time'] + '')
        conn = psycopg2.connect(database = 'bittrex', user = 'postgres', password = 'niyeyede', host = '52.78.21.186', port = '5432')
        cur = conn.cursor()
        cur.execute('INSERT INTO usdt_btc_onemin(time,open,high,low,close,volume,bv) '
                    'VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');' % (Item['Time'],Item['Open'],Item['High'],Item['Low'],Item['Close'],Item['Volume'],Item['BV']))
        conn.commit()
        conn.close()
 ##       with open('history.csv','a+',newline='') as f:
 ##           writer = csv.writer(f)
 ##           writer.writerow(data)
        return Item
