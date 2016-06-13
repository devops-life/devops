#!/usr/bin/env python
# encoding: utf-8



from app import db
from app.models import User


user = User('admin','admin','chen_zhangpeng@163.com')
db.session.add(user)
db.session.commit()