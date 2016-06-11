#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: captcha.py
@time: 16-6-10 上午1:01
"""


from flask import Blueprint, request, make_response, abort
import StringIO
import json
from tools.captcha import Captcha
from tools.token import Token


captcha_bp = Blueprint('captcha', __name__, url_prefix='/captcha')

params = {
    'size': (68, 28),
    'fg_color': (180, 180, 180),
    'line_color': (100, 100, 100),
    'point_color': (100, 100, 100)
}
captcha_client = Captcha(**params)


@captcha_bp.route('/')
def index():
    """
    首页
    http://localhost:8011/
    """
    return 'captcha page'


@captcha_bp.route('/get_token/<code_type>/')
def get_token(code_type):
    """
    获取 token
    http://localhost:8011/captcha/get_token/reg/      # 注册
    http://localhost:8011/captcha/get_token/login/    # 登录
    http://localhost:8011/captcha/get_token/reg_bad/  # 错误
    """
    if code_type not in ['reg', 'login']:
        abort(404)
    token_client = Token(code_type)
    token = token_client.create_token()
    return token


@captcha_bp.route('/check_token/<code_type>/<token>/')
def check_token(code_type, token):
    """
    校验 token
    http://localhost:8011/captcha/check_token/reg/abcdefg.123456/
    """
    if code_type not in ['reg', 'login']:
        abort(404)
    token_client = Token(code_type)
    result = token_client.check_token(token)
    return json.dumps(result)


@captcha_bp.route('/get_code/<code_type>/<token>/')
def get_code(code_type, token):
    """
    http://localhost:8011/captcha/get_code/reg/abcdefg/?t=1234
    """
    if code_type not in ['reg', 'login']:
        abort(404)
    # 校验 token
    check_result = check_token(code_type, token)
    check_result = json.loads(check_result)
    if 'error' in check_result:
        abort(401)
    uuid_str = check_result.get('success')
    code_img, code_str = captcha_client.get()
    # 保存 code_str
    token_client = Token(code_type)
    token_client.add_item(uuid_str, code_str)
    # 返回验证码图片
    buf = StringIO.StringIO()
    code_img.save(buf, 'JPEG', quality=70)
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    return response


@captcha_bp.route('/check_code/<code_type>/<token>/')
def check_code(code_type, token):
    """
    校验验证码
    http://localhost:8011/captcha/check_code/reg/abcdefg/?code_str=7E6G
    """
    if code_type not in ['reg', 'login']:
        abort(404)
    code_str = request.args.get('code_str', '', type=str)
    token_client = Token(code_type)
    code_str_result = token_client.get_item(token)
    token_client.del_item(token)
    return json.dumps({'result': code_str == code_str_result})


@captcha_bp.errorhandler(404)
def page_not_found(error):
    # return render_template('404.html'), 404
    return '404.html', 404
