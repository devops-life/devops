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
from models import db
#注意蓝图的导入方式
from app.views.home import home
from app.views.admin import admin
from flask_login import LoginManager

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    #读取配置
    app.config.from_object("config")
    app.config.from_pyfile("config.py")
    #
    init_login(app)
    register_blueprints(app)
    register_database(app)

    return app
#注册蓝图
def register_blueprints(app):
    app.register_blueprint(home,url_prefix='/home')
    app.register_blueprint(admin,url_prefix='/admin')

#初始化数据库
def register_database(app):
    db.init_app(app)

#设置flask-login
def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.objects(id=user_id).first()



