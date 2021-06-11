import requests

pre_url = "http://pan.baidu.com/rest/2.0/xpan/file?method=precreate&access_token=123.bcb7b19f9dcd0ee2f6657d3be5053d8b.YHNlJcpujF5LOUoZB-gctHdl5ZAe72AJKZWdR2S.tDoo9g"
payload = {'path': '/apps/eth/eth/2021/5',
           'size': '0',
           'isdir': '1',
           'autoinit': '1',
           'rtype': '3',
           'block_list': '["e08b8e863d2fffce685530608305598c"]'}
response = requests.request("POST", pre_url, data=payload)
print(response.text.encode('utf8'))