#coding=gbk

"""
网页爬虫常用来在互联网上爬取感兴趣的页面或文件，结合数据处理与分析技术可以得到更深层次
的信息。下面的代码实现了网页爬虫，可以抓取网页中的所有链接，并且可以指定关键字和抓取深
度
"""
import sys
import multiprocessing
import re
import os
import urllib.request as lib
def craw_links(url, depth, keywords, processed):
    '''url:the url to craw
    depth:the current depth to craw
    keywords:the tuple of keywords to focus
    pool:process pool
    '''
    contents = []
    if url.startswith(('http://', 'https://')):
        if url not in processed:
            # mark this url as processed
            processed.append(url)
        else:
            # avoid processing the same url again
            return
    print('Crawing' + url + '……')
    fp = lib.urlopen(url)
    #Python 3 returns bytes, so need to decode
    contents_decoded = contents.decode('utf-8')
    fp.close()
    pattern = '|'.join(keywords)
    # if this page contains certain keywords, save it to a file
    flag = False
    if pattern:
        searched = re.search(pattern, contents_decoded)
    else:
        # if the keywords to filter is not given, save current page
        flag =True
    if flag or searched:
        with open('craw\\' + url.replace(':', '_').replace('/','_'),'wb') as fp:
            fp.write(contents)
    # find all the links in the current page
    links = re.findall('href = "(.*?)', contents_decoded)
    # craw all links in thr current page
    for link in links:
        # consider rhe relative path
        if not link.startswith(('http://','https://')):
            try:
                index = url.rindex('/')
                link = url[0:index+1] + link
            except:
                pass
        if depth > 0 and link.endswith(('.htm', '.html')):
            craw_links(link, depth -1, keywords, processed)

if __name__ == '__main__':
    processed = []
    keywords = ('datetime', 'KeyWord2')
    if not os.path.exists('craw') or not os.path.isdir('craw'):
        os.mkdir('craw')
    craw_links(r'https://docs.python.org/3/library/index.html', 1, keywords, processed)
