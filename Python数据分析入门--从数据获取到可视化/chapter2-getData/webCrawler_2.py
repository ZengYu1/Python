# coding=utf-8
"""
模拟登陆：
通过cookie的方式来检验用户的登陆状态，可以直接从浏览器复制cookie到headers来进行模拟登陆
"""
import requests
from fake_useragent import UserAgent

mycookie_fromcopy = 'bid=wVfHNJJBYIY; douban-fav-remind=1; ll="118281"; ' \
                    'gr_user_id=889423ee-16fd-4cbf-9885-18f56af7e8be; ' \
                    '_vwo_uuid_v2=D5A95789929A99155A2012362ADCAB408|7dbd37f39a2d3d0b55a32e9258b3660d; ' \
                    '__utmz=30149280.1551800325.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/;' \
                    ' viewed="30389631"; __utma=30149280.251264901.1546785126.1551800325.1552105986.4; __utmc=30149280; ' \
                    '__utmt=1; __utmb=30149280.4.9.1552106165753; dbcl2="168256310:2RqXmJ8VB/M"; ck=1LQx; ap_v=0,6.0'
ua = UserAgent()
headers = {
    'User-Agent':ua.random,
    'Cookie':mycookie_fromcopy
}

#这里是登录之后才能访问到的个人信息页面
url = "https://www.douban.com/people/168256310/"
data = requests.get(url, headers = headers)

print(data.status_code)
print(data.request.headers)
print(data.text)