#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: models.py
@time: 16/6/8 下午2:25
"""

from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)

    def __init__(self,username,password,email):
        self.username = username
        self.set_password(password)
        self.email = email

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return '&lt;User %r>' % self.username