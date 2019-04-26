# coding=utf-8
"""
使用正则表达式提取字符串中的电话号码
"""
import re

telNumber = '''Suppose my Phone No. is 0535-1234567,yours is 010-12345678,his is 025-87654321.'''
pattern = re.compile(r'(\d{3,4})-(\d{7,8})')
index = 0
while True:
    matchResult = pattern.search(telNumber,index)   #从指定位置开始匹配
    if not matchResult:
        break
    print('-'*30)
    print('Success:')
    for i in range(3):
        print('Search content:', matchResult.group(i),\
              'Start from:',matchResult.start(i),'End at:',matchResult.end(i),\
              'Its span is:',matchResult.span(i))
    index = matchResult.end(2)