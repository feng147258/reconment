#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 2:18 PM
# @Author  : Yingjun Zhu
# @File    : user.py

class UserId():
    __tablename__ = 'corpus_result_detail'

    # id = db.Column(db.Integer, primary_key=True)
    # tenant_id = db.Column(db.Integer)
    # robot_id = db.Column(db.Integer)
    # corpus_id = db.Column(db.Integer)
    # message1 = db.Column(db.String(516), default="noMessage1")
    # message2 = db.Column(db.String(516), default="noMessage2")
    # status = db.Column(db.Integer, default=1)
    # results = db.Column(db.String(32), default="noLable")

    def __repr__(self):
        return '<Coupus %r>' % self.message1