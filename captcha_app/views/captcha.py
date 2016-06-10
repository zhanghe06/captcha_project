#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: captcha.py
@time: 16-6-10 上午1:01
"""


from flask import Blueprint, request, make_response
import StringIO
from tools.captcha import Captcha


captcha_bp = Blueprint('captcha', __name__, url_prefix='/captcha')


@captcha_bp.route('/')
def index():
    return 'captcha page'


@captcha_bp.route('/code/')
def get_code():
    """
    http://localhost:8011/captcha/code/?t=1234
    """
    # 把 code_str 发给前端,或者在后台使用 session 保存
    params = {
        'size': (68, 28),
        'fg_color': (180, 180, 180),
        'line_color': (100, 100, 100),
        'point_color': (100, 100, 100)
    }
    captcha = Captcha(**params)
    code_img, code_str = captcha.get()
    buf = StringIO.StringIO()
    code_img.save(buf, 'JPEG', quality=70)

    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    return response


@captcha_bp.route('/code/check/')
def check_code():
    """
    校验验证码
    http://localhost:8011/captcha/code/check/?code_str=7E6G
    """
    code_str = request.args.get('code_str', '', type=str)
    return code_str

