#coding=gbk
import urllib.request
import urllib.parse
"""
下面的代码演示了如何使用GET方法读取并显示指定URL的内容
"""
# params = urllib.parse.urlencode({'spam':1, 'eggs':2, 'bacon':0})
# url = "http://www.musi-cal.com/cgi-bin/query?%s"%params
# with urllib.request.urlopen(url) as f:
#     print(f.read().decode('utf-8'))

"""
下面的代码演示了如何读取并显示指定网页的内容
"""
# fp = urllib.request.urlopen(r'http://www.python.org')
# print(fp.read(100))
# print(fp.read(100).decode())
# fp.close()

"""
下面的代码演示了如何使用POST方法提交参数并读取指定页面内容
"""
# data = urllib.parse.urlencode({'spam':1, 'eggs':2, 'bacon':0})
# data = data.encode('ascii')
# with urllib.request.urlopen("http://requestb.in/xrb182xr", data) as f:
#     print(f.read().decode('utf-8'))

"""
下面的代码演示了如何使用HTTP代理访问的指定页面
"""
proxies = {'http':'http://proxy.example.com:8080/'}
opener = urllib.request.FancyURLopener(proxies)
with opener.open("http://www.python.org") as f:
    f.read().decode('utf-8')
