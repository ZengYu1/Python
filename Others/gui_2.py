from tkinter import *
def showmsg():
    label1.config(text='单击了按钮！')
label1 = Label(text='你好,Python!')
label1.pack()
Button(text='按纽',command = showmsg).pack()
mainloop()