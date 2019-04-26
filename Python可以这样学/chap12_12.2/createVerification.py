#coding=gbk
"""
������֤��ͼƬ
"""
from PIL import Image, ImageDraw, ImageFont
import random
import string

#���п��ܵ��ַ�����Ҫ��Ӣ����ĸ������
characters = string.ascii_letters + string.digits

#��ȡָ�����ȵ��ַ���
def selectedCharacters(length):
    '''length:the number of characters to show'''
    result = ""
    for i in range (length):
        result += random.choice(characters)
    return result

def getColor():
    '''get a random color'''
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def main(size = (200,100), characterNumber = 6, bgcolor = (255,255,255)):
    imageTemp = Image.new('RGB', size, bgcolor)
    #����������ֺ�
    font = ImageFont.truetype('c:\\windows\\fonts\\TIMESBD.TTF',48)
    draw = ImageDraw.Draw(imageTemp)
    text = selectedCharacters(characterNumber)
    width, height = draw.textsize(text,font)
    #������֤���ַ���
    offset = 2
    for i in range(characterNumber):
        offset += width//characterNumber
        position = (offset,(size[1] - height) // 2 + random.randint(-10,10))
        draw.text(xy = position, text=text[i], font=font, fill=getColor())
    #����֤��ͼƬ���м򵥱任��������ü򵥵ĵ�����
    imageFinal = Image.new('RGB',size,bgcolor)
    pixelsFinal = imageTemp.load()
    pixelsTemp = imageTemp.load()
    for y in range (0, size[1]):
        offset = random.randint(-1,1)
        for x in range(0,size[0]):
            newx = x + offset
            if newx >= size[0]:
                newx = size[0] - 1
            elif newx < 0:
                newx = 0
            pixelsFinal[newx, y] = pixelsTemp[x,y]
    draw = ImageDraw.Draw(imageFinal)
    #���Ƹ����������
    for i in range (int(size[0] * size[1] * 0.07)):
        draw.point((random.randint(0, size[0]), random.randint(0, size[1])), fill=getColor())
        #���Ƹ�������
        for i in range(8):
            start = (0, random.randint(0, size[1] - 1))
            end = (size[0], random.randint(0, size[1] - 1))
            draw.line([start,end], fill=getColor(),width=1)
        #���Ƹ��Ż���
        for i in range(8):
            start = (-50,-50)
            end = (size[0] + 10, random.randint(0, size[1] + 10))
            draw.arc(start + end, 0, 360, fill=getColor())
        #������֤��ͼƬ
        imageFinal.save("result.jpg")
        imageFinal.show()

if __name__ == '__main__':
    main((200, 100), 8, (255, 255, 255))
