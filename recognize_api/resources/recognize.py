#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: recognize.py
@time: 16-6-10 上午1:01
"""


from flask_restful import Resource


class Recognize(Resource):
    def get(self, img_url=None):
        """
        http://localhost:8012/recognize
        http://localhost:8012/recognize/python
        """
        return {'hello': img_url if img_url is not None else 'world'}
