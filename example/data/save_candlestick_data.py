import os
from datetime import date
import time
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market.candlestick_event import CandlestickEvent




def callback(candlestick_event: 'CandlestickEvent'):
    today = date.today()
    file_path = '/data/eth/' + today.year + '/' + (today.month + 1)
    try:
        os.makedirs(file_path, mode=0o770)
    except FileExistsError as e:
        print(e)

    file_name = time.strftime("%Y-%m-%d", time.localtime())
    with open(file_path + "/" + file_name, "a+") as f:
        f.write(candlestick_event.ts + "," + candlestick_event.ch +"," +candlestick_event.tick.open+
                ","+candlestick_event.tick.high, +","+ candlestick_event.tick.low + "," +candlestick_event.tick.close
                +"," + candlestick_event.tick.amount, +","+candlestick_event.tick.vol)


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)

market_client = MarketClient()
market_client.sub_candlestick("ethusdt", CandlestickInterval.MIN1, callback, error)