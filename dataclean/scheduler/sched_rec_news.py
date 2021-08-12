#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 4:45 PM
# @Author  : Yingjun Zhu
# @File    : sched_rec_news.py
from dataclean.read_data.read_news_data import NewsData
from dataclean.models.recall.item_base_cf import ItemBaseCF


class SchedRecNews(object):
    def __init__(self):
        self.new_data = NewsData()
        self.item_base_cf = ItemBaseCF()

    def sched_task(self):
        """
        定时任务：计算得分、模型训练、推荐并入库
        :return:
        """
        # 计算得分，明确给谁计算得分（明确推荐用户列表）， 推荐分为冷启动和模型推荐
        # 推荐用户列表：暂定为 用过 app 且有阅读记录的
        user_list = self.new_data.get_rec_users()


    def cal_score(self):
        pass

    def rec_list(self, user_id):
        """
        返回 user_id 的推荐列表
        :return:
        """
        pass

    def to_redis(self):
        pass
