#coding=gbk
from PIL import Image
from PIL import ImageGrab
from PIL import ImageFilter

#��ͼ���ļ�
# im = Image.open('��Ů.png')
# im.show()
# print(im.format)
# print(im.size)
# print(im.height + im.width)
# im.histogram()            #���ͼ��������ͨ�����򷵻�����ͨ����ֱ��ͼ
# im.histogram()[:256]      #�鿴��һ��ͨ����ֱ��ͼ
# im.getpixel((150,80))       #����������Ԫ�飬����Ԫ�طֱ��ʾx��y����
# im.putpixel((100,50),(128,30,120))      #�ڶ�����������ָ��Ŀ�����ص���ɫֵ
# im.save('��Ů2.jpg')          #���԰�ͼ�񱣴�Ϊ��һ���ļ�����и�ʽת��
# im= im.resize((100,100))       #ͼ�����ţ�������ʾͼ����³ߴ磬��ʾ��͸�
#
# im = ImageGrab.grab((0,0,800,200))        #��Ļ��ͼ
# im.show()
im = Image.open('��Ů.png')
im = im.filter(ImageFilter.BLUR)
# im = im.filter(ImageFilter.GaussianBlur)    #��˹ģ��
# im = im.filter(ImageFilter.MedianFilter)    #��ֵ�˲�
# im = im.point(lambda i:i *1.5)      #�������
# im = im.point(lambda i: i * 1.8 if i < 100 else i * 0.7)    #�Զ������ͼ��������

im.show()

