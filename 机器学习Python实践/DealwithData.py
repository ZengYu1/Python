# coding=utf-8
filename = 'pima_data.txt'
myfile = 'pima_data.csv'
fl = open(filename, 'r+')
mf = open(myfile, 'w+')
data = fl.read()
rows = data.split(' ')
full_data = []
for row in rows:
    split_now = row.split(",")
    full_data.append(split_now)
    mf.read(split_now)



fl.close()
mf.close()

