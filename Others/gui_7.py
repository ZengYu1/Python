from tkinter import *
label1 = Label(text = '标签')
label1.pack()

def show1():
    label1.config(text = bt1.cget('text'))

def show2():
    label1.config(text = bt2.cget('text'))

str = '按纽1\n带位图的按纽'

bt1 = Button(bitmap = 'info', text = str)
bt1.config(compound = LEFT, justify = RIGHT, width = 200,
           height = 50, bd = 3, relief = RAISED, anchor = W,
           font = ('隶书',-20), command = show1, activebackground = 'yellow',
           activeforeground = 'red')
bt1.pack()

bt2 = Button(text = '按纽2')
bt2.config(width = 10, bd = 3, relief = RAISED, wraplength = 300,
           anchor = CENTER, font = ('楷体',20,'underline'), command = show2)
bt2.pack()

mainloop()