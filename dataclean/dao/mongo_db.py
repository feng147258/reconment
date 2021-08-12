#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 6:35 PM
# @Author  : zhuyingjun
# @File    : mongo_db.py

import pymongo


class MongoDB(object):
    def __init__(self, db=None,collentions =None):
        mongo_client = self._connect('localhost', 27017, '', '', db)
        self.db_client = mongo_client[db]  #使用 recommend_test 库
        self.collection = self.db_client[collentions]   #使用 test_collentions 集合


    def _connect(self, host, port, user, pwd, db):
        mongo_info = self._splicing(host, port, user, pwd, db)
        mongo_client = pymongo.MongoClient(mongo_info, connectTimeoutMS=12000, connect=False)
        return mongo_client

    @staticmethod
    def _splicing(host, port, user, pwd, db):
        client = 'mongodb://' + host + ":" + str(port) + "/"
        if user != '':
            client = 'mongodb://' + user + ":" + pwd + "@" + host + ":" + str(port) + "/"
            if db != '':
                client += db
        return client

    def test_insert(self):
        test_collection = dict()
        test_collection["name"] = 'junge'
        test_collection['age'] = 18
        test_collection['sex'] = 'man'
        self.collection_test.insert_one(test_collection)


if __name__ == "__main__":
    mongo = MongoDB()
    mongo.test_insert()
