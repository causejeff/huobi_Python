from huobi.client.market import MarketClient
from huobi.utils import *

market_client = MarketClient(api_key="56f62d38-3f50e5a3-ed2htwf5tf-5083d", secret_key="20718585-1111d314-fda942fa-d161d", url="https://api.huobi.pro")
list_obj = market_client.get_market_trade(symbol="eosusdt")
LogInfo.output_list(list_obj)












