#coding=gbk
from pyecharts import Bar
import pyecharts_jupyter_installer

columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

#设置柱状图的主标题和副标题
bar = Bar("柱状图", "一年的降水量与蒸发量")
#添加柱状图的数据和配置项
bar.add("降水量", columns, data1, mark_line = ["average"], mark_point = ["max", "min"])
bar.add("蒸发量", columns, data2, mark_line = ["average"], mark_point = ["max", "min"])

#生成本地文件(默认为.html文件)
bar.render()