# coding=gbk
from csv import reader
import numpy as np
from numpy import loadtxt
from pandas import read_csv
# ���ñ�׼��⵼������
# filename = 'iris.data.csv'
# with open(filename, 'rt') as raw_data:
#     readers = reader(raw_data, delimiter = ',')
#     x = list(readers)
#     data = np.array(x)
#     print(data.shape)

##����Numpy��������
# filename = 'iris.data.csv'
# with open(filename, 'rt') as raw_data:
#     data = loadtxt(raw_data, delimiter=',')
#     print(data.shape)


##����Pandas��������
filename = 'iris.data.csv'
names = ['preg', 'plas', 'pres', 'skin', '����']
data = read_csv(filename, names=names)
print(data.shape)

