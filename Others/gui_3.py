from tkinter import *
def onLeftClick(event):
    label1.config(text = '单击了鼠标左键！')
    print('单击了鼠标左键！')

def onRightClick(event):
    label1.config(text = '单击了鼠标右键！')
    print('单击了鼠标右键')

def onDoubleLeftClick(event):
    label1.config(text = '双击了鼠标左键！')
    print('双击了鼠标左键！')

def onLeftDrag(event):
    label1.config(text = '按下鼠标拖动！鼠标位置(%s.%s)' % event.char)
    print('按下鼠标拖动!鼠标位置(%s,%s)' % (event.x,event.y))

def onReturn(event):
    label1.config(text = '按下了【Enter】键！')
    print('按下了【Enter】键！')

def onKeyPress(event):
    label1.config(text = '按下了键盘的 %s 键！' % event.char)
    print('按下了键盘上的 %s 键！' % event.char)

def onArrowPress(event):
    label1.config(text = '按下了【Up】')
    print('按下了【Up】键')

label1 = Label(text = '你好，Python')
label1.pack()
bt1 = Button(text = '按纽')
bt1.bind('<Button-1>',onLeftClick)
bt1.bind('Button-3>',onRightClick)
bt1.bind('<Double-1>',onDoubleLeftClick)
bt1.bind('<B1-Motion>',onLeftDrag)
bt1.bind('<Return>',onReturn)
bt1.bind('<KeyPress>',onKeyPress)
bt1.bind('<Up>',onArrowPress)
bt1.pack()
bt1.focus()             #使按纽获得焦点
mainloop()
