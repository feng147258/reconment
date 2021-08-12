#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 1:51 PM
# @Author  : Yingjun Zhu
# @File    : read_news_data.py
from dataclean.dao.mongo_db import MongoDB
# from dataclean.dao.mysql_db import Mysql
import os

class NewsData(object):

    def __init__(self):

        self.mongo = MongoDB(db="loginfo", collentions='read')
        self.db_loginfo = self.mongo.db
        self.read_collection = self.mongo.collection


    def get_data_from_mongodb(self):
        result = list()
        read_data = self.read_collection.find()
        for item in read_data:
            result.append(str(item['user_id'+",1,"+str(item["content_id"])]))

        self.to_csv(result,'../data/news_score/news_log.csv')

    def to_csv(self,user_data , w_file):
        if not os.path.exists("../data/news_score"):
            os.makedirs("../data/news_score")
        with open(w_file,'w',encoding="utf-8") as wf:
            for data in  user_data:
                wf.write(data+"\n")

    def get_rec_users(self):
        data = self.read_collection.distinct("user_id")

        return data
