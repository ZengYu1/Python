#coding=gbk
import urllib.request
import urllib.parse
"""
����Ĵ�����ʾ�����ʹ��GET������ȡ����ʾָ��URL������
"""
# params = urllib.parse.urlencode({'spam':1, 'eggs':2, 'bacon':0})
# url = "http://www.musi-cal.com/cgi-bin/query?%s"%params
# with urllib.request.urlopen(url) as f:
#     print(f.read().decode('utf-8'))

"""
����Ĵ�����ʾ����ζ�ȡ����ʾָ����ҳ������
"""
# fp = urllib.request.urlopen(r'http://www.python.org')
# print(fp.read(100))
# print(fp.read(100).decode())
# fp.close()

"""
����Ĵ�����ʾ�����ʹ��POST�����ύ��������ȡָ��ҳ������
"""
# data = urllib.parse.urlencode({'spam':1, 'eggs':2, 'bacon':0})
# data = data.encode('ascii')
# with urllib.request.urlopen("http://requestb.in/xrb182xr", data) as f:
#     print(f.read().decode('utf-8'))

"""
����Ĵ�����ʾ�����ʹ��HTTP������ʵ�ָ��ҳ��
"""
proxies = {'http':'http://proxy.example.com:8080/'}
opener = urllib.request.FancyURLopener(proxies)
with opener.open("http://www.python.org") as f:
    f.read().decode('utf-8')
