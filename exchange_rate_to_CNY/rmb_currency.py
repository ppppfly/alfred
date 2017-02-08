# coding=utf-8
import json
import sys
import urllib2
from decimal import *


def parse(strs):
    res = {"title": strs, "subtitle": "Copy to clipboard", "arg": strs, "icon": "icon.png"}
    return json.dumps({"items": [res]})


query = sys.argv[1]
args = query.split(' ')

if len(args) <= 1 or len(args[1]) == 0:
    print parse('请输入 金额')
    sys.exit(0)

elif not str(args[1]).isdigit():
    print parse('第二个参数 请输入金额（数值）')
    sys.exit(0)

currency, amount = query.split(' ')

url = 'http://webforex.hermes.hexun.com/forex/quotelist?code=FOREX{}CNY&column=price'.format(currency.upper())
req = urllib2.Request(url)
resp = urllib2.urlopen(req)
json_str = resp.read()
rate = str(json_str).lstrip('({"Dat:[').rstrip(']});')

rate = rate if rate else 0

result = Decimal(amount) * Decimal(rate) / Decimal(10000)

print(parse('￥{0:.2f}'.format(result)))
