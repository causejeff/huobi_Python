import os
from datetime import date
import time
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market.candlestick_event import CandlestickEvent
file_path = "/Users/zhouyuan/data/2021/5/"
files = os.listdir("file_path")
for file in files:
    with open(file_path+file, "r") as f:
        f.readline()