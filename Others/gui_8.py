#coding:gb2312
"""
�ó���ʵ����һ���򵥵ĵ�½���ڣ��������û��������룬���������á���Ŧ�������������û���
�����룬����ȷ����Ŧ�ɽ�������û�����������ʾ���·����ı�����
"""
from tkinter import *
fup = Frame()   #��һ��������ڷ���������Ͷ�Ӧ����ʾ��ǩ
fup.pack()

username = StringVar()  #���ڰ��û����������
password = StringVar()  #���ڰ������������

#ִ���û���У������ĺ���
def usercheck(what):
    if len(what) > 10:
        label3.config(text = '�û������ܳ���10���ַ�', fg = 'red')
        return False
    return True

#ִ������У������ĺ���
def passwordcheck(why,what):
    if why == '1':
        if what not in '0123456789':
            label3.config(text = '����ֻ��������', fg = 'red')
            return False
        return True

label1 = Label(fup, text='�û���:', width = 8, anchor = E)
label1.grid(row = 1, column = 2)
entry1 = Entry(fup, textvariable = username, width = 20)    #�û����������
docheck1 = entry1.register(usercheck)   #ע��У�麯��
entry1.config(validate = 'all', validatecommand = (docheck1,'%P'))  #����У�����
entry1.grid(row = 1, column = 2)

label2 = Label(fup, text = '���룺', width = 8, anchor = E)
label2.grid(row = 2, column = 2)
entry2 = Entry(fup, show = '*', textvariable = password, width = 20)    #�����������
docheck2 = entry2.register(passwordcheck)   #ע��У�麯��
entry2.config(validate = 'all', validatecommand = (docheck2,'%d','%S'))  #����У�����
entry2.grid(row = 2, column = 2)


def reset():
    entry1.delete(0, END)
    password.set('')
    label3.config(text = '')

def done():
    label3.config(text = '��������û���Ϊ��%s,����Ϊ��%s' % (username.get(), password.get()))

fdown = Frame()
fdown.pack()
bt1 = Button(fdown, text = '����', command = reset)
bt1.grid(row = 1, column = 1)

bt2 = Button(fdown, text = 'ȷ��', command = done)
bt2.grid(row = 1, column = 2)

label3 = Label()
label3.pack()

mainloop()