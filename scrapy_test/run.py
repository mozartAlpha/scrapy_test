from subprocess import Popen, STDOUT
import time

cmd = 'scrapy crawl bittrex-usdt-btc'

while True:
    Popen(cmd)
    time.sleep(120)



