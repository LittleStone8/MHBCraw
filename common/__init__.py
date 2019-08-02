from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
'''
proxy='221.229.196.152:19600'  #使用本地代理
#proxy='username:password@123.58.10.36:8080'  #购买代理
proxy_handler=ProxyHandler({
    'http':'http://'+proxy,
    'https':'https://'+proxy
})
opener=build_opener(proxy_handler)
try:
    response=opener.open('https://recommd.xyq.cbg.163.com/cgi-bin/recommend.py?callback=Request.JSONP.request_map.request_0&_=1562818151825&act=recommd_by_role&server_id=39&areaid=33&server_name=%E4%B8%96%E7%95%8C%E4%B9%8B%E7%AA%97&page=2&kindid=23&view_loc=equip_list&count=15&order_by=unit_price%20ASC') #测试ip的网址
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
'''
