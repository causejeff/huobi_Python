import os
from datetime import date
import time
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market.candlestick_event import CandlestickEvent

today = date.today()
global_file_path = '/data/eth/' + str(today.year) + '/' + str(today.month)
global_file_name = time.strftime("%Y-%m-%d", time.localtime())
current_file_name = global_file_name

try:
    os.makedirs(global_file_path, mode=0o770)
except FileExistsError as e:
    pass

current_file = open(global_file_path + "/" + global_file_name, "a+")

exist_path = {global_file_path: 1}


def callback(candlestick_event: 'CandlestickEvent'):
    file_path = '/data/eth/' + str(today.year) + '/' + str(today.month)
    file_name = time.strftime("%Y-%m-%d", time.localtime())
    is_exist = exist_path[file_path]
    if not is_exist:
        try:
            os.makedirs(file_path, mode=0o770)
            exist_path[file_path] = 1
        except FileExistsError as e:
            pass
    global current_file_name
    if current_file_name != file_name:
        global current_file
        current_file.flush()
        current_file.close()
        current_file = open(file_path + "/" + file_name, "a+")
        current_file_name = file_name

    content = (time.strftime("%Y-%m-%d %H:%M", time.localtime(candlestick_event.ts / 1000)) + "," +
               str(candlestick_event.ts) + "," + str(candlestick_event.tick.open) + "," +
               str(candlestick_event.tick.high) + "," + str(candlestick_event.tick.low) + "," +
               str(candlestick_event.tick.close) + "," + str(candlestick_event.tick.amount) + "," +
               str(candlestick_event.tick.vol) + "\n")
    current_file.write(content)


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)

market_client = MarketClient()
market_client.sub_candlestick("ethusdt", CandlestickInterval.MIN1, callback, error)