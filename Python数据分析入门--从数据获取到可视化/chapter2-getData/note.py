# coding=utf-8

#获取动态UA
# from fake_useragent import UserAgent
#
# ua = UserAgent()
# print(ua.chrome)
# print(ua.ie)
# print(ua.firefox)
# print(ua.random)

#代理IP
# import requests
# proxies = {
#     "http":"125.88.74.122:84",
#     "http":"123.84.13.240:8118",
#     "https":"94.240.33.242:3128"
# }
# data = requests.get("http://icanhazip.com", proxies = proxies)
# print(data)

#编码检测
import requests
data = requests.get('http://www.baidu.com')
# print(data.text)

import chardet
charset = chardet.detect(data.content)  #检测编码
print(charset)                          #返回一个字典类型，包含两个键，一个是编码方式，一个是本页检测的可行度
data.encoding = charset['encoding']     #指定编码
print(data.text)