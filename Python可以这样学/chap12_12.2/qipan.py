#coding=gbk
"""ʹ��pillow���ɹ���������������"""
from PIL import Image

def qipan(fileName, width, height, color1, color2):
    #���ɿհ�ͼ��
    im = Image.new('RGB', (width,height))
    for h in range(height):
        for w in range(width):
            #�����ɫ�����ͼ��
            if (int(h / height * 25) + int(w / width * 16)) % 2 == 0:
                im.putpixel((w,h),color1)
            else:
                im.putpixel((w,h), color2)
    #����ͼ���ļ�
    im.save(fileName)

if __name__ == '__main__':
    fileName = 'qipan.jpg'
    qipan(fileName, 500, 500, (128,128,128),(10,10,10))
