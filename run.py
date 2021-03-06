#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: run.py
@time: 16/6/13 下午4:55
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)