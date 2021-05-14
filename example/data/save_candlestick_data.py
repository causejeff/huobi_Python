import os
from datetime import date
import time
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market.candlestick_event import CandlestickEvent




def callback(candlestick_event: 'CandlestickEvent'):
    today = date.today()
    file_path = '/data/eth/' + str(today.year) + '/' + str(today.month)
    try:
        os.makedirs(file_path, mode=0o770)
    except FileExistsError as e:
        print(e)
    file_name = time.strftime("%Y-%m-%d", time.localtime())
    with open(file_path + "/" + file_name, "a+") as f:
        content = (time.strftime("%Y-%m-%d %H:%M", candlestick_event.ts) + "," +
                   str(candlestick_event.ts) + "," + str(candlestick_event.tick.open) + "," +
                   str(candlestick_event.tick.high) + "," + str(candlestick_event.tick.low) + "," +
                   str(candlestick_event.tick.close) + "," + str(candlestick_event.tick.amount) + "," +
                   str(candlestick_event.tick.vol) + "\n")
        f.write(content)


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)

market_client = MarketClient()
market_client.sub_candlestick("ethusdt", CandlestickInterval.MIN1, callback, error)