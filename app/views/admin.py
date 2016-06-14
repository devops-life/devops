#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: admin.py
@time: 16/6/13 下午6:22
"""


from flask import Blueprint,render_template

#新建蓝图
admin = Blueprint('admin',__name__)

@admin.route('/')
def index():
    return 'admin'