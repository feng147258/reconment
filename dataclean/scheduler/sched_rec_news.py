#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 4:45 PM
# @Author  : Yingjun Zhu
# @File    : sched_rec_news.py


class SchedRecNews(object):
    def __init__(self):
        pass

    def sched_task(self):
        """
        定时任务：计算得分、模型训练、推荐并入库
        :return:
        """
        pass

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
