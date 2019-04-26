# coding=utf-8
##简单查看数据
from pandas import read_csv
#显示数据的前十行
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
peek = data.head(10)
print(peek)
print(data.dtypes)  ##数据属性和类型
print(data.shape)   ##数据的维度

##描述性统计
from pandas import set_option
set_option('display.width', 100)
#设置数据的精确度
set_option('precision',4)
print(data.describe())

##数据分组分布（适用于分类算法）
print(data.groupby('class').size())

##数据属性的相关性
setattr('display.width', 100)
#设置数据精度
set_option('precision', 2)
print(data.corr(method='pearson'))
"""
在机器学习中，当数据的关联性比较高时，有些算法的性能会降低，所以在开始训练算法
前，查看算法的关联性是一个很好的方法；
pearson()
常通用的计算两个属性的相关性的方法是皮尔逊相关系数。皮尔逊相关系数是度量
两个变量间相关程度的方法;1表示完全正相关，0表示不相关，-1表示完全负相关
"""

##数据分布分析
#计算数据的高斯偏离
"""
skew()函数的结果显示了数据分布是左偏还是右偏，当数据接近0时，表示数据的偏差非常小
"""
print(data.skew())