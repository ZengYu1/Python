#coding=gbk
import os
import os.path
import time

def FileSplit(sourceFile, targetFolder):
    if not os.path.isfile(sourceFile):      #Դ�ļ��������
        print(sourceFile, 'does not exist.')
        return
    if not os.path.isdir(targetFolder):     #Ŀ���ļ��������򴴽�
        os.mkdir(targetFolder)
    tempData = []           #���������ʱ����
    number = 25           #�зֺ��ÿ��С�ļ�����1000��
    fileNum = 1     #�зֺ���ļ����
    with open(sourceFile, 'r') as srcFile:
        dataLine = srcFile.readline().strip()
        while dataLine:
            for i in range(number):     #��ȡ1000���ı�
                tempData.append(dataLine)
                dataLine = srcFile.readline()
                if not dataLine:
                    break
            desFile = os.path.join(targetFolder, sourceFile[0:-4] + str(fileNum) + '.txt')
            with open(desFile, 'a+') as f:      #����һ��С�ļ�
                f.writelines(tempData)
            tempData = []
            fileNum = fileNum + 1           #С�ļ���ż�1

if __name__ == '__main__':
    sourceFile = 'test.txt'         #ָ��Դ�ļ�
    targetFolder = 'test'           #ָ������зֺ�С�ļ����ļ���
    FileSplit(sourceFile, targetFolder)