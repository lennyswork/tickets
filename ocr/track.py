#!/usr/bin/env python3
from configparser import ConfigParser
from PIL import Image
import pytesser3
def main():
    im = Image.open('../picture/file.bmp')
    imgry = im.convert('L')
    # imgry.show()
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    out.show()
    im1 = Image.open('../picture/large.png')
    print(pytesser3.image_to_string(im))
    # print(pytesser3.image_file_to_string('../picture/file.jpg'))








if __name__ == '__main__':
    print('*'*20 + "track" + '*'*20)
    print(dir(pytesser3.Image))
    print(dir(Image))
    main()