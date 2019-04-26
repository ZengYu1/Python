#coding=gbk
"""使用pillow生成国际象棋棋盘纹理"""
from PIL import Image

def qipan(fileName, width, height, color1, color2):
    #生成空白图像
    im = Image.new('RGB', (width,height))
    for h in range(height):
        for w in range(width):
            #填充颜色交叉的图案
            if (int(h / height * 25) + int(w / width * 16)) % 2 == 0:
                im.putpixel((w,h),color1)
            else:
                im.putpixel((w,h), color2)
    #保存图像文件
    im.save(fileName)

if __name__ == '__main__':
    fileName = 'qipan.jpg'
    qipan(fileName, 500, 500, (128,128,128),(10,10,10))
