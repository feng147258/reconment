#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 5:47 PM
# @Author  : Yingjun Zhu
# @File    : lfm.py

import random
import math
from tqdm import tqdm



class LFM(object):

    def __init__(self, train_file, F, alpha=0.01, beta=0.1, max_iter=500):
        """
        :param train_file: 用于存放训练数据的文件
        :param F: 隐因子个数
        :param alpha: 学习率
        :param beta: 正则化系数
        :param max_iter:最大迭代次数
        """
        self.F = F
        self.P = dict()  # R=PQ^T，代码中的Q相当于博客中Q的转置
        self.Q = dict()
        self.train_data = dict()
        self.alpha = alpha
        self.beta = beta
        self.max_iter = max_iter
        self.get_data(train_file)

    def get_data(self, train_file):
        """
        :param train_file:
        :return:
        """
        with open(train_file, 'r', encoding='utf-8') as rf:
            for line in tqdm(rf.readlines()):
                user, rating, item = line.strip().split(",")
                self.train_data.setdefault(user, {})
                self.train_data[user][item] = float(rating)

    def train(self):
        """
        随机梯度下降法训练参数P和Q
        :return:
        """

        for step in range(self.max_iter):
            for user, rates in self.train_data.items():
                for item, rui in rates.items():
                    '''随机初始化矩阵P和Q'''
                    if user not in self.P:  # 暂时做成 读取的数据放到内存中
                        self.P[user] = [random.random() / math.sqrt(self.F) for x in range(self.F)]
                    if item not in self.Q:
                        self.Q[item] = [random.random() / math.sqrt(self.F) for x in range(self.F)]

                    hat_rui = self.predict(user, item)
                    err_ui = rui - hat_rui
                    for f in range(self.F):
                        self.P[user][f] += self.alpha * (err_ui * self.Q[item][f] - self.beta * self.P[user][f])
                        self.Q[item][f] += self.alpha * (err_ui * self.P[user][f] - self.beta * self.Q[item][f])
            self.alpha *= 0.9  # 每次迭代步长要逐步缩小

    def predict(self, user, item):
        """
        :param user:
        :param item:
        :return:
        预测用户user对物品item的评分
        """
        return sum(self.P[user][f] * self.Q[item][f] for f in range(self.F))


    def cal_recall(self, user, topK=30):
        """
        计算召回,推荐给 user 对应的 item
        :param user:
        :param topK:取前 k 个
        :return:  推荐给 user 的 items list
        [('b', 0.5817461814808832), ('d', 0.5531647388889103), ('c', 0.2832831339855817), ('a', 0.24726583603934602)]
        """
        record = {}
        if user not in self.P:
            return []

        for item in self.Q:
            res = self.predict(user, item)
            record[item] = res

        rec_list = sorted(record.items(), key=lambda x :x[1], reverse=True)[0:topK]

        return rec_list


if __name__ == '__main__':

    '''用户有A B C，物品有a b c d'''
    train_file = "../../data/test_lfm.txt"
    lfm = LFM(train_file, 2)
    lfm.train()
    for item in ['a', 'b', 'c', 'd']:
        print(item, lfm.predict('B', item))  # 计算用户A对各个物品的喜好程度
    print(lfm.cal_recall("B",50))