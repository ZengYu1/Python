#coding=gbk

"""
scrapy��һ���ǳ����õ�web�����ܣ��ǳ��ʺ�ץȡwebվ�����ҳ����ȡ�ṹ�������ݣ�����֧���Զ���������ʹ��scrapy��ȥ��ҳ����ʱ��
������ϤHTML��ǩ������Ҫ�˽�Ŀ����ҳ��������֯�ṹ��ȷ��Ҫ��ȡʲô��Ϣ����������������Եر�д�������
"""

import os
import urllib.request
import scrapy

class MySpider(scrapy.spiders.Spider):
    #��������֣�ÿ�����涼�����в�ͬ������
    name = 'mySpider'
    allowed_domains={'http://www.sdibt.edu.cn/info/1026/11238.htm'}

    #��ÿһ��Ҫ��ȡ��ҳ�棬���Զ����������������
    def parse(self, response):
        self.downloadWebpage(response)
        self.downloadImages(response)

        #���ҳ���еĳ����ӣ���������ȡ
        hxs = scrapy.Selector(response)
        sites = hxs.xpath('//ul/li')
        for site in sites:
            link = site.xpath('a/@herf').extract()[0]
            if link == '#':
                continue
            #����Ե�ַת���ɾ��Ե�ַ
            elif link.startswith('..'):
                next_url = os.path.dirname(response.url)
                next_url += '/' + link
            else:
                next_url = link
            #����Request���󣬲�ָ���ص�����
            yield scrapy.Request(url = next_url, callback = self.parse_item)
    #�ص�����������ʼҳ���е�ÿ��������������
    def parse_item(self, response):
        self.downloadWebpage(response)
        self.downloadImage(response)

    #���ص�ǰҳ��������ͼƬ
    def downloadIamge(self,response):
        hxs = scrapy.Selector(response)
        images = hxs.xpath('//img/@src').extract()
        for image_url in images:
            imageFilename = image_url.split('/')[-1]
            if os.path.exists(imageFilename):
                continue
            #����Ե�ַת���ɾ��Ե�ַ
            if iamge_url.startswith('..'):
                image_url = os.path.dirname(response.url) + '/' + image_url
            #����ҳͼƬ
            fp = urllib.request.urlopen(iamge_url)
            #��������ͼƬ�ļ�
            with open(imageFilename, 'wb') as f:
                f.write(fp.read())
            fp.close()

    #����ҳ���ݱ���Ϊ�����ļ�
    def downloadWebpage(self, response):
        filename = response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

