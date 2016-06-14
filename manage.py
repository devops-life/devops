#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: manage.py.py
@time: 16/6/8 下午2:26
"""

from flask_script import Manager,Server
from app import create_app

app = create_app()
manager = Manager(app)
manager.add_command("runserver",Server(host='0.0.0.0',port=5000))


if __name__ == '__main__':
    manager.run()