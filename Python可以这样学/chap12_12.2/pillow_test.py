#coding=gbk
from PIL import Image
from PIL import ImageGrab
from PIL import ImageFilter

#打开图像文件
# im = Image.open('美女.png')
# im.show()
# print(im.format)
# print(im.size)
# print(im.height + im.width)
# im.histogram()            #如果图像包含多个通道，则返回所有通道的直方图
# im.histogram()[:256]      #查看第一个通道的直方图
# im.getpixel((150,80))       #参数必须是元组，两个元素分别表示x和y坐标
# im.putpixel((100,50),(128,30,120))      #第二个参数用来指定目标像素的颜色值
# im.save('美女2.jpg')          #可以把图像保存为另一个文件或进行格式转换
# im= im.resize((100,100))       #图像缩放，参数表示图像的新尺寸，表示宽和高
#
# im = ImageGrab.grab((0,0,800,200))        #屏幕截图
# im.show()
im = Image.open('美女.png')
im = im.filter(ImageFilter.BLUR)
# im = im.filter(ImageFilter.GaussianBlur)    #高斯模糊
# im = im.filter(ImageFilter.MedianFilter)    #中值滤波
# im = im.point(lambda i:i *1.5)      #整体变亮
# im = im.point(lambda i: i * 1.8 if i < 100 else i * 0.7)    #自定义调整图像明暗度

im.show()

