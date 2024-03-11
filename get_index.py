# 使用腾讯股票api获取创业板指数历史数据

import requests
import json
import pandas as pd


def get_stock(date):
    url = 'http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=sz399006,day,2015-12-01,%s,2000,bfq' % date
    r = requests.get(url)
    raw_data = json.loads(r.text)
    print(raw_data)
    data = raw_data['data']['sz399006']['day']
    return data

data1 = get_stock('2024-01-27')

df = pd.DataFrame(data1, columns=['Date', 'Open', 'Close', 'High', 'Low', 'Trans'])
df = df[::-1].reset_index(drop=True)

df.to_csv('sz399006.csv',index=False)
