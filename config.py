#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: config.py.py
@time: 16/6/8 下午2:26
"""

SECRET_KEY = "\xbb\x99P\x9e\x8bm\xf13\xed<\x187\x9e\x18O\xff\xc7\x8c\x99\x00"
DEBUG = True
SQLALCHEMY_DATABASE_URI='mysql://root:QQ_bb@2016@127.0.0.1/devops'
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False
