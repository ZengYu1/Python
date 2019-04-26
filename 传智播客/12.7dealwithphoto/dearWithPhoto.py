# coding: utf-8
import Image
import os

myPath = "source/"
outPath = "destination/"


def processImage(filesource, destsource, name, imgtype):
    imgtype = "jpeg" if imgtype == ".jpg" else "png"
    im = Image.open(filesource + name)

    rate = max(im.size[0]/640.0 if im.size[0] > 640 else 0,
               imsize[1]/1136.0 if im.size > 1136 else 0)
    if rate:
        im.thumbnail((im.size[0]/rate, im.size[1]/rate))
    im.save(destsource + name, imgtype)


def run():
    os.chdir(myPath)
    for i in os.listdir(os.getcwd()):
        postfix = os.path.splittext(i)[1]
        if postfix == '.jpg' or postfix == '.png':
            processImage(myPath, outPath, i, postfix)

if __name__ == '__main__':
	run()