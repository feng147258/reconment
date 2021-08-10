#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 3:30 PM
# @Author  : Yingjun Zhu
# @File    : simple_rec.py
'''
从 Mongo中，按照时间顺序去数据
'''
import datetime
from dataclean.dao import redis_db
from dataclean.dao.mongo_db import MongoDB


class SimpleRecList(object):
    def __init__(self):
        self._redis = redis_db.MyRedis()
        self.mongo = MongoDB(db="loginfo", collentions='content_collentions')
        self.db_loginfo = self.mongo.db
        self.collection = self.mongo.collection

    def get_news_order_by_time(self):
        data = self.collection.find().sort([{"$news_data",-1}])
        count = 10000
        for new in data:
            self._redis.redis.zadd("rec_list",{str(new["_id"]):count})
            count -= 1
            if count % 10 == 0:
                print(count)
