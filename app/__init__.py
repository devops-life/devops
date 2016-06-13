#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: __init__.py
@time: 16/6/8 下午2:25
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views.home import home


app = Flask(__name__,instance_relative_config=True)
#注册蓝图
app.register_blueprint(home)

#读取隐藏配置文件和配置文件
app.config.from_object("config")
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)

from app import views,models