#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 6:41 PM
# @Author  : Yingjun Zhu
# @File    : redis_db.py

import redis


class MyRedis(object):
    def __init__(self):

        self.redis = redis.StrictRedis(host='127.0.0.1',port =6379,
                                       password="123456",
                                       db=1,
                                       decode_responses=True
                                       )