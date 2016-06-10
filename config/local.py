#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: local.py
@time: 16-3-10 下午5:10
"""

# 数据库
DB = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '123456',
    'db': 'test',
    'port': 3306
}
SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
    (DB['user'], DB['passwd'], DB['host'], DB['port'], DB['db'])
SQLALCHEMY_POOL_SIZE = 50  # 默认 pool_size=5


REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

