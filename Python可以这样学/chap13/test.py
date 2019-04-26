#coding=gbk
import numpy as np
import matplotlib.pylab as pl
x = np.random.random(100)
y = np.random.random(100)
pl.scatter(x,y,s=y * 500,c=u'b',marker=u'*')
pl.show()