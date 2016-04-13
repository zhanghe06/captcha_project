#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: recognize.py
@time: 16-4-11 下午9:30
"""


from PIL import Image
import pytesseract


class Recognize(object):
    """
    图像识别（验证码）
    """
    def __init__(self, img_name):
        self.img_name = img_name
        self.img_fp = Image.open(self.img_name)
        self.img_text = ''

    def optimize_img(self):
        """
        对图片预处理，提高识别率
        :return:
        """
        # 转化为灰度图像
        img_gray = self.img_fp.convert('L')
        img_gray.save(self.img_name)
        # 二值化
        threshold = 220  # 灰度阀值（阀值越高，得到的图像噪点越多；阀值越低，后面获取的有效颜色越少）
        table = []
        for i in range(256):
            if i < 10:
                # 去干扰线的关键（将接近黑色干扰线颜色填充为白色）
                table.append(1)
            elif i < threshold:
                # 将颜色亮度低于阀值的有效颜色填充为黑色
                table.append(0)
            else:
                # 将颜色亮度高于阀值的颜色填充为白色
                table.append(1)
        out = img_gray.point(table, '1')
        out.save(self.img_name)
        self.img_fp = out

    def crop_img(self, width=80, height=23, border=1):
        """
        裁剪图片，去掉边框（裁剪边框可减少干扰度，提高识别率）
        :param width:图片宽度
        :param height:图片高度
        :param border:边框厚度
        :return:返回裁剪后的图片对象
        """
        box = (border, border, width - border * 2, height - border * 2)
        new_img = self.img_fp.crop(box)
        new_img.save(self.img_name)
        self.img_fp = new_img

    def optimize_text(self):
        """
        对于识别成特殊符号的 采用该表进行修正
        :return:返回修正后的字符串
        """
        self.img_text = self.img_text.strip()
        self.img_text = self.img_text.upper()
        rep = {
            ' ': '',
            '.': '',
            ',': '',
            '‘': 'C',
            '(': 'C',
            '（': 'C',
            '$': 'S',
        }
        # TODO:待完善
        self.img_text = ''.join([str(rep.get(item, item)) for item in self.img_text])

    def img_to_string(self):
        """
        图片转为字符串
        :return:
        """
        # 图片裁剪
        self.crop_img()
        # 图片优化
        self.optimize_img()
        # 图片识别
        self.img_text = pytesseract.image_to_string(self.img_fp)
        # 文本优化
        print '优化前字符：%s' % self.img_text
        self.optimize_text()
        print '优化后字符：%s' % self.img_text


if __name__ == '__main__':
    print(pytesseract.image_to_string(Image.open('/home/zhanghe/code/captcha_project/images/6716.jpg')))
    print(pytesseract.image_to_string(Image.open('/home/zhanghe/code/captcha_project/images/Y4N6.gif')))
