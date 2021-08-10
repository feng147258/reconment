#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 2:59 PM
# @Author  : Yingjun Zhu
# @File    : mongo_to_redis.py

import pymongo
from dataclean.dao import redis_db
from dataclean.dao.mongo_db import MongoDB


class WriteToRedis(object):
    def __abs__(self):
        self._redis = redis_db.MyRedis()
        self.mongo = MongoDB(db="loginfo", collentions='content_collentions')
        self.db_loginfo = self.mongo.db
        self.collection = self.mongo.collection

    def get_data_from_mongoDB(self):
        piplines = [{
            '$group': {
                '_id': '$type'
            }
        }]
        types = self.collection.aggregate(piplines)
        for type in types:
            # print(type['_id'])
            cx = {"type": type['_id']}
            data = self.collection.find(cx)
            for info in data:
                result = dict()
                result['describe'] = str(info['describe'])
                result['type'] = str(info['type'])
                result['news_date'] = str(info['news_date'])
                result["content_id"]= str(info["_id"])

                result['likes'] = info['likes']
                result['read'] = info['read']
                result['hot_heat'] = info['hot_heat']
                result["collections"] = info["collections"]

                self._redis.redis.set("news_datail:" + str(info['_id']), str(result))
                self._redis.redis.zadd()

if __name__ == '__main__':
    write2redis = WriteToRedis()
    write2redis.get_data_from_mongoDB()
