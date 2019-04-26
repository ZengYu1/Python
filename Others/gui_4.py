from tkinter import *
label1 = Label(text = '标签1')
label1.config(fg = 'white', bg = 'black')
label2 = Label(text = '标签2')
label2.config(fg = 'red', bg = 'yellow')
label3 = Label(text = '标签3')
label3.config(fg = 'white', bg = 'green')

"""
Packer布局
ipadx 或 iapdy：组件内部左右或上下边框预留空白宽度
padx 或 pady：组件外部左右或边框预留空白宽度
"""
# label1.pack(anchor = NE)
# label3.pack(anchor = N)
# label2.pack(anchor = SW)

"""
Grid布局
rowspan：组件占用的行数
columnspan：组件占用的列数
sticky：组件在单元格内的对齐方式，可用常量为N、S、W、E、NW、SW、NE、SE 和CENTER
与pack()方法的anchor参数值一致
ipadx 或 ipady：组件内部左右或上下边框预留空白位置
padx 或 pady：组件外部左右或上下边框预留空白位置
"""
# label1.grid(row = 0, column = 0, rowspan = 5, columnspan = 8, ipadx = 200,
#            ipady = 200, padx = 100, pady = 100)
# label2.grid(row = 1, column = 2)
# label3.grid(row = 2, column = 1)

"""
Place布局
使用Place可以与Grid布局和Packer布局同时使用
place()方法常用参数
anchor
bordermode：指定在计算位置时，是否包含容器外界宽度，默认为INSIDE(计算容器边界)，
OUTSIDE表示不计算容器边界
height、width：指定组件的高度和宽度，坐标默认为像素
relheight、relwidth：按容器高度和宽度的比例来指定组件的高度和宽度，取值范围为0.0-1.0
x，y：用绝对坐标指定组件的位置，坐标默认单位为像素
relx、rely：按容器高度和宽度的比例来指定组件的位置，取值范围为0.0-1.0
在使用坐标时，容器左上角为原点
"""
label1.place(x = 0, y = 0)
label2.place(x = 50, y = 50)
label3.place(relx = 0.5, rely = 0.5)
mainloop()