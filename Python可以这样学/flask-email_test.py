#coding=gbk
"""
Python+Flask+flask-email���ʹ������ĵ����ʼ�
"""
import os.path
from flask import Flask
from flask.ext.mail import Mail, Message

app = Flask(__name__)
#��126�������Ϊ��
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
#������������ַ��15813384764@126.com,��ôӦ��д15813384764
app.config['MAIL_USERNAME'] = '1114586754@qq.com'
app.config['MAIL_PASSWORD'] = 'huangzengyue1'

def sendEmail(From, To, Subject, Body, Html, Attachments):
    '''To:must be a list'''
    msg = Message(Subject, sender = From, recipients = To)
    msg.body = Body
    msg.html = Html
    for f in Attachments:
        with app.open_resource(f) as fp:
            msg.attach(filename=os.path.basename(f), data=fp.read(),
                               content_type='application/octet-stream')
    mail = Mail(app)
    with app.app_context():
        mail.send(msg)

if __name__ == '__main__':
    #From��д�ĵ��������ַ������ǰ�����õ���ͬ
    From = '<1114586754@qq.com>'
    To = ['<15813384764@126.com>']
    Subject = 'hello world'
    Body = 'Only a test.'
    Html = '<h1>test test test.</h1>'
    Attachments = ['D:\Programing\Anaconda\python.exe']
    sendEmail(From, To, Subject, Body, Html, Attachments)