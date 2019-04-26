# coding=utf-8
import requests
import pickle
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def get_cookie_from_net():
    url = 'http://accounts.douban.com/login'
    #构建表单
    payload = {
        'source':'None',
        'redir':'http://www.douban.com/',
        'form_email':'15813384764',
        'form_password':'123456',
        'login':'登录'
    }
    data = s.post(url, headers=headers, data=payload, verify=True) #绕过了SSL验证
    with open('cookie.douban','wb') as f:
        cookiedict = requests.utils.dict_from_cookiejar(s.cookies)
        pickle.dump(cookiedict,f)
    print("提交表单登录，成功获取cookies……")

    return s.cookies

#从cookie文件获取cookie
def get_cookie_from_file():
    with open('cookie.douban','rb') as f:
        cookiedict = pickle.load(f)
        cookies = requests.utils.cookiejar_from_dict(cookiedict)
    print("解析文件，成功提取cookies……")
    return cookies

#假设这里要获取自己的签名数据
def get_data(html):
    soup = BeautifulSoup(html.text, 'lxml')
    mydata = soup.select('#display')[0].get_text()
    '''
    这里进行登录后其他数据的获取及存储，这里仅仅获取自己的签名数据
    '''
    return mydata


def login_and_getdata():
    print('获取cookies……')
    try:
        s.cookies = get_cookie_from_file()
    except:
        print("从文件获取cookies失败……\n正在尝试提交表单登录以获取……")
        s.cookies = get_cookie_from_net()
    html =  s.get('https://www.douban.com/people/168256310/',headers=headers)
    #print(html.text)
    data = get_data(html)
    print(data)

if __name__ == '__main__':
    #一些全局变量
    s = requests.session()
    ua = UserAgent()
    headers = {'User-Agent':ua.random}

    #登录并获取数据
    login_and_getdata()