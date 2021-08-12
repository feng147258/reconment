#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 1:47 PM
# @Author  : Yingjun Zhu
# @File    : logData.py

from dataclean.dao.mongo_db import MongoDB
from dataclean.dao import redis_db
from datetime import datetime

class LogData(object):

    def  __init__(self):
        self._mongo = MongoDB(db="loginfo", collentions='content_collentions')

        self._redis = redis_db.MyRedis()

    def insert_log(self,user_id,content_id,title,tables):
        """
        将数据写入到 mongo 中。本项目中是从 mysql 校验后确定存在的一条数据
        :param user_id:
        :param content_id:
        :param title:
        :param tables: 数据写入到 name为tables 的表中
        :return:
        """

        collections = self._mongo.db_client[tables]
        info = dict()
        info["user_id"] = user_id
        info["content_id"] = content_id
        info["title"] = title
        info["data"] = datetime.utcnow()

        collections.insert_one(info)

    def get_logs(self):

        pass

    def modify_articles_details(self,key,ops):
        """
        redis 取数据，修改 ops 的值，再写入 redis
        :param key:
        :param ops:
        :return:
        """

        info  = self._redis.get(key)
        info = eval(info)
        info[ops] +=1
        self._redis.redis.set(key,str(info))




