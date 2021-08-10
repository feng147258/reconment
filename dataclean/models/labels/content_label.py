#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 7:12 PM
# @Author  : zhuyingjun
# @File    : content_label.py
import re
from dao.mongo_db import MongoDB
from dao.mysql_db import Mysql
from dao.redis_db import MyRedis
from datetime import datetime
from models.keywords.tf_idf import Segment
from sqlalchemy import distinct
from models.labels.entity.content import Content
'''
ContentLable 
'''

class ContentLabel(object):
    def __init__(self):
        mongo_db = MongoDB(db='content_labels')
        self.seg = Segment(stopword_files=[], userdict_files=[])
        self.engine = Mysql()
        self.session = self.engine._DBSession()
        self.mongo = MongoDB(db="loginfo",collentions='content_collentions')
        self.db_loginfo = self.mongo.db
        self.collection = self.mongo.collection


    def get_data_from_mysql_to_mongo(self):
        '''
        从mysql 中取出数据，计算好关键词、及词的个数等，并存入到 Mongo 中
        :return:
        '''
        types = self.session.query(distinct(Content.type))
        for i in  types:
            res = self.session.query(Content).filter(Content.type == i[0])
            if res.count() >0:
                for x in res.all():
                    keywords = self.get_keywords(x.content,10)
                    word_nums = self.get_word_nums(x.content)
                    times = x.time
                    creat_time = datetime.utcnow()
                    content_collection= dict()
                    content_collection['describe']=x.content
                    content_collection['keywords'] = keywords
                    content_collection['word_num'] = word_nums
                    content_collection['new_date'] = times
                    content_collection['hot_heat'] = 10000
                    content_collection['type'] = x.type

                    content_collection['likes'] = 0         #点赞
                    content_collection['read'] = 0          #阅读
                    content_collection['collection'] = 0    #收藏

                    content_collection['creatr_time'] = creat_time
                    self.collection.insert_ont(content_collection)


    def get_keywords(self, contents, nums=10):
        keywords = self.seg.extract_keyword(contents)[:nums]
        return keywords

    def get_type(self):
        return

    def get_news_type(self):
        return

    def get_word_nums(self, contents):
        ch = re.findall('[\u4e00-\u9fa5]', contents)
        nums = len(ch)
        return nums

    def insert_to_mongodb(self, contents):
        content_label_dict = dict()
        collection = 'content_label'
        times = datetime.time()
        content_label_dict['name'] = 'junge'
        content_label_dict['time'] = times
        content_label_dict['keywords'] = self.get_keywords(contents)
        content_label_dict['words_nums'] = self.get_word_nums(contents)


    def get_data_from_mysql(self):
        return


if __name__ == '__main__':
    content_label = ContentLabel()
    keywords = content_label.get_keywords(contents="今天天气很好呀", nums=3)
    print(keywords)
    nums = content_label.get_word_nums(contents="今天天气很好呀")

    print(nums)
