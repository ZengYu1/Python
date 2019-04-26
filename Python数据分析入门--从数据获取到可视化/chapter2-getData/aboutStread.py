# coding=utf-8
import  re
import requests
import pandas as pd
from fake_useragent import UserAgent

url = 'http://www.hao123.com/'
ua = UserAgent()
headers = {'User-Agent':ua.random}

resp = requests.get(url, headers)
data = resp.text
urls = re.findall(r'href=(http.*?)',data)
print(len(urls))

df = pd.DataFrame()

df['url'] = urls[:1000]
df.to_csv('TestUrls.csv',index=None)