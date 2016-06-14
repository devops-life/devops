#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: forms.py
@time: 16/6/13 下午4:54
"""
from flask_wtf import Form
from wtforms import  StringField,PasswordField
from wtforms.validators import DataRequired,Email

class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])