#!/usr/bin/env python3
from configparser import ConfigParser
from PIL import Image

def main():
    im = Image.open('../picture/file.bmp')
    imgry = im.convert('L')
    imgry.show()
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    out.show()






if __name__ == '__main__':
    print('*'*20 + "track" + '*'*20)
    main()
