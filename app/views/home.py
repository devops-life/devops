#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: home.py
@time: 16/6/13 下午6:22
"""

from flask import Blueprint,render_template

#新建蓝图
home = Blueprint('home',__name__)

@home.route('')
def index():
    render_template('home/index.html')