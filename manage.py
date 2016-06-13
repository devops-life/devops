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
from app import app,db
from app.models import User

manager = Manager(app)
manager.add_command("runserver",Server(host='0.0.0.0',port=5000))

#测试db连接
@manager.command
def save_User():
    user = User('111','1111@qq.com')
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()