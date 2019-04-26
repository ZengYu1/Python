#coding=gbk
import os
import os.path
import time

def FileSplit(sourceFile, targetFolder):
    if not os.path.isfile(sourceFile):      #源文件必须存在
        print(sourceFile, 'does not exist.')
        return
    if not os.path.isdir(targetFolder):     #目标文件不存在则创建
        os.mkdir(targetFolder)
    tempData = []           #用来存放临时数据
    number = 25           #切分后的每个小文件包含1000行
    fileNum = 1     #切分后的文件编号
    with open(sourceFile, 'r') as srcFile:
        dataLine = srcFile.readline().strip()
        while dataLine:
            for i in range(number):     #读取1000行文本
                tempData.append(dataLine)
                dataLine = srcFile.readline()
                if not dataLine:
                    break
            desFile = os.path.join(targetFolder, sourceFile[0:-4] + str(fileNum) + '.txt')
            with open(desFile, 'a+') as f:      #创建一个小文件
                f.writelines(tempData)
            tempData = []
            fileNum = fileNum + 1           #小文件编号加1

if __name__ == '__main__':
    sourceFile = 'test.txt'         #指定源文件
    targetFolder = 'test'           #指定存放切分后小文件的文件夹
    FileSplit(sourceFile, targetFolder)