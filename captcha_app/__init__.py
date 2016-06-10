#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 16-6-10 上午12:41
"""


from flask import Flask
from .views.captcha import captcha_bp


app = Flask(__name__)

app.register_blueprint(captcha_bp)
