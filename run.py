#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: captcha.py
@time: 16-3-31 上午9:21
"""


from tools.captcha import Captcha
import StringIO
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'test'


def get_token():
    """
    获取 token
    """
    uid = '006002'
    channel = 'reg'
    sign = ''
    token = ''
    return token


@app.route('/code/')
def get_code():
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
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    return response


@app.route('/code/check/')
def check_code():
    """
    校验验证码
    http://localhost:18888/code/check/?code_str=7E6G
    """
    code_str = request.args.get('code_str', '', type=str)
    return code_str


if __name__ == "__main__":
    app.run(host="localhost", port=18888, debug=True)
