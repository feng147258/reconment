#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 6:59 PM
# @Author  : Yingjun Zhu
# @File    : pageData.py
from dataclean.dao import redis_db


class PageData(object):
    def __init__(self):
        self._redis_db = redis_db.MyRedis()

    def get_page_data(self, page_size, page_num):
        start = (page_num - 1) * page_size
        end = page_num * page_size - 1
        datas = self._redis_db.redis.zrange("rec_list", start, end)
        lst = list()
        for data in datas:
            print(data)
            result = self._redis_db.redis.get("new_detail:"+data)
            lst.append(data)
        return  lst


if __name__ == '__main__':
    page_data = PageData()
    page_data.get_page_data(10, 3)
