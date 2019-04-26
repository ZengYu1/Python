#coding=gbk
import os
import re
import threading
import time

def Map(sourceFile):                        #这段代码仅适用于配套文件
    if not os.path.exists(sourceFile):
        print(sourceFile, 'does not exist.')
        return
    pattern = re.compile(r'[0-9]{1,2}/[0-9]{4}')
    result = []
    with open(sourceFile, 'r') as srcFile:
        for dataLine in srcFile:
            r = pattern.findall(dataLine)       #查找符合日期格式的字符串
            if r:
                result[r[0]] = result.get(r[0], 0) + 1
    desFile = sourceFile[0:-4] + '_map.txt'
    with open(desFile, 'a+') as fp:
        for k, v in result.items():
            fp.write(k + ':' + str(v) + '\n')

if __name__ == '__main__':
    desFolder = 'test'
    files = os.listdir(desFolder)
    def Main(i):
        Map(desFolder + '\\' + files[i])
    fileNumber = len(files)
    for i in range (fileNumber):
        t = threading.Thread(target=Main, args=(i,))
        t.start()