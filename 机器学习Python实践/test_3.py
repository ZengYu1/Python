import numpy as np
import pandas as pd
myarray = np.array([1, 2, 3])
index = ['a', 'b', 'c']
myseries = pd.Series(myarray, index = index)
print(myseries)
print('Series中的第一个元素')
print(myseries[0])
print('Series中的 c index元素')
print(myseries['c'])

#DataFrame是一个可以指定行和列标签的二维数组。数据可以通过指定列名来访问特定列的数据
myarray = np.array([[1, 2, 3],
                    [2, 3, 4],
                    [3, 4, 5]])
rowindex = ['row1', 'row2', 'row3']
colname = ['col1', 'col2', 'col3']
mydataframe = pd.DataFrame(data=myarray, index=rowindex, columns=colname)
print(mydataframe)
print('访问col3的数据')
print(mydataframe['col3'])
