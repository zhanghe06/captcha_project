#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 16-6-10 下午11:19
"""


from flask import Flask
from flask_restful import Api
from recognize_api.resources.recognize import Recognize


app = Flask(__name__)
api = Api(app)

api.add_resource(Recognize, '/recognize', '/recognize/<string:img_url>')
