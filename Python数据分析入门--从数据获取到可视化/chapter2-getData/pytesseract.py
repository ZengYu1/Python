# coding=utf-8

import pytesseract
from PIL import Image
print('hello')
image = Image.open('1.png')
vcode = pytesseract.image_to_string(image)
Image._show(image)
print(vcode)