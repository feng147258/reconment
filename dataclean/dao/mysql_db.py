#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 6:35 PM
# @Author  : Yingjun Zhu
# @File    : mysql_db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base


class Mysql (object):
    def __init__(self):
        Base  = declarative_base()
        self.engine = create_engine("mysql+pymysql://root:zhu,8283115@127.0.0.1:3306/reconmend",encoding="utf-8")
        self._DBSession = sessionmaker()