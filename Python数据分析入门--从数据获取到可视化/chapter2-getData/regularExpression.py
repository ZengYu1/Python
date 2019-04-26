# coding=utf-8
import re
import requests
from fake_useragent import UserAgent
import chardet

ua = UserAgent()
headers = {'User-Agent':ua.random}
#headers = {}
html = requests.get('http://www.baidu.com',headers = headers)
charset = chardet.detect(html.content)
html.encoding = charset['encoding']
print(html)
print(11111111)
html = html.text
print(html)
print(2222222)
title = re.findall(r'<a href="(http://.*?.com)" name="tj_tr.*?" class="mnav">(\w{2})</a>', html)
print(title)
print(3333333)
