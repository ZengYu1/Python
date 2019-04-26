# coding=utf-8
import urllib.robotparser

import requests

urls = ["http://www.baidussfghdhs.com", "http://news.baidu.com/", "http://datahonor.com/404", "http://httpstat.us/500"]

def get_data(url):
    try:
        data = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print("请求错误，url:", url)
        print("错误详情:",e)
        data = None
    print(data)

def robot_check(robotstxt_url, headers, url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotstxt_url)
    rp.read()
    result = rp.can_fetch(headers['User-Agent'], url)
    return result

if __name__ == '__main__':
    for url in urls:
        if robot_check(robotstxt_url, headers, url):
            get_data(url)
# print(data)a