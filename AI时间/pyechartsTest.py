#coding=gbk
from pyecharts import Bar
import pyecharts_jupyter_installer

columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

#������״ͼ��������͸�����
bar = Bar("��״ͼ", "һ��Ľ�ˮ����������")
#�����״ͼ�����ݺ�������
bar.add("��ˮ��", columns, data1, mark_line = ["average"], mark_point = ["max", "min"])
bar.add("������", columns, data2, mark_line = ["average"], mark_point = ["max", "min"])

#���ɱ����ļ�(Ĭ��Ϊ.html�ļ�)
bar.render()