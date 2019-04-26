# coding utf-8
##直方图
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix

filename = 'iris.data.txt'
names = ['preg', 'plas', 'pres', 'skin', 'test']
data = read_csv(filename, names=names)
data.hist()
plt.show()

##密度图
data.plot(kind = 'density', subplots = True, layout = (3, 3), sharex = False)
plt.show()

##箱型图
data.plot(kind = 'box', subplots = True, layout = (3, 3), sharex = False)

###多重图表
##相关矩阵图
correlations = data.corr()
fig = plt.figure()
ax = fig.add_subplot()
cax = ax.matshow(correlations, vmin = -1, vmax = 1)
fig.colorbar(cax)
ticks = np.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()


##散点矩阵图
scatter_matrix(data)
