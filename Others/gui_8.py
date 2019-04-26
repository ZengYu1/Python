#coding:gb2312
"""
该程序实现了一个简单的登陆窗口，可输入用户名和密码，单击“重置”按纽可清除已输入的用户名
和密码，单击确定按纽可将输入的用户名和密码显示在下方的文本框中
"""
from tkinter import *
fup = Frame()   #第一个框架用于放输入组件和对应的提示标签
fup.pack()

username = StringVar()  #用于绑定用户名输入组件
password = StringVar()  #用于绑定密码输入组件

#执行用户名校验操作的函数
def usercheck(what):
    if len(what) > 10:
        label3.config(text = '用户名不能超过10个字符', fg = 'red')
        return False
    return True

#执行密码校验操作的函数
def passwordcheck(why,what):
    if why == '1':
        if what not in '0123456789':
            label3.config(text = '密码只能是数字', fg = 'red')
            return False
        return True

label1 = Label(fup, text='用户名:', width = 8, anchor = E)
label1.grid(row = 1, column = 2)
entry1 = Entry(fup, textvariable = username, width = 20)    #用户名输入组件
docheck1 = entry1.register(usercheck)   #注册校验函数
entry1.config(validate = 'all', validatecommand = (docheck1,'%P'))  #设置校验参数
entry1.grid(row = 1, column = 2)

label2 = Label(fup, text = '密码：', width = 8, anchor = E)
label2.grid(row = 2, column = 2)
entry2 = Entry(fup, show = '*', textvariable = password, width = 20)    #密码输入组件
docheck2 = entry2.register(passwordcheck)   #注册校验函数
entry2.config(validate = 'all', validatecommand = (docheck2,'%d','%S'))  #设置校验参数
entry2.grid(row = 2, column = 2)


def reset():
    entry1.delete(0, END)
    password.set('')
    label3.config(text = '')

def done():
    label3.config(text = '你输入的用户名为：%s,密码为：%s' % (username.get(), password.get()))

fdown = Frame()
fdown.pack()
bt1 = Button(fdown, text = '重置', command = reset)
bt1.grid(row = 1, column = 1)

bt2 = Button(fdown, text = '确定', command = done)
bt2.grid(row = 1, column = 2)

label3 = Label()
label3.pack()

mainloop()