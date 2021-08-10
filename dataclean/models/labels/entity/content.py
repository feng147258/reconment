#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 7:48 PM
# @Author  : Yingjun Zhu
# @File    : content.py

from  sqlalchemy import Column ,String ,Integer,DateTime,Text
from  sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Content(Base):
    __tablename__ ="data"

    id = Column(Integer,primary_key=True)
    time = Column(DateTime)
    title = Column(Text())
    content = Column(Text())
    type = Column(Text())

    def __init__(self):

        pass


