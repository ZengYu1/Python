"""
bd:指定边框宽度
relief：指定边框样式，可用RAISED(凸起)、SUNKEN(凹陷)、FLAT(扁平)、RIDGE(脊状)
GROOVE(凹槽)和SOLID(实线)
width、height：设置宽度和高度，通常被忽略，容器通常根据内容组件的大小自动调整自身大小
"""
from tkinter import *
root = Tk()
frame1 = Frame(bd = 200, relief = SUNKEN)
frame2 = Frame(bd = 4, relief = RAISED)
label1 = Label(frame1, text = '标签1', fg = 'white', bg = 'black')
label2 = Label(frame1, text = '标签2', fg = 'red', bg = 'yellow')
label3 = Label(frame1, text = '标签3', fg = 'white', bg = 'green')
label4 = Label(frame2, text = '标签4', fg = 'blue', bg = 'gray')
label5 = Label(frame2, text = '标签5', fg = 'orange', bg = 'white')
label6 = Label(frame2, text = '标签6', fg = 'white', bg = 'green')

#框架1 和框架2 在默认主窗口中使用Packer布局
frame1.pack()
frame2.pack()
#标签1、2、3在框架1中使用Packer布局
label1.pack()
label2.pack(side = LEFT)
label3.pack(side = RIGHT)
#标签4、5、6在框架2中使用Grid布局
label4.grid(row = 1, column = 1)
label5.grid(row = 3, column = 4)
label6.grid(row = 2, column = 2)

root.mainloop()
