# coding utf-8
import urllib.request
import urllib
# import urllib3

"""
基本抓取网页
"""

"""
get方法

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
print(response.read())

"""

# post方法

url = "http://abcde.com"
form = {'name':'abc','password':'1234'}
form_data = urllib.request.urlencode(form)
request = urllib.request.Request(url, form_data)
response = urllib.request.urlopen(request)
print(request.read())


