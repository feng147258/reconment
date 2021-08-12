#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 4:29 PM
# @Author  : Yingjun Zhu
# @File    : item_base_cf.py
import math
from tqdm import tqdm
import sys

sys.path.append("..")


class ItemBaseCF(object):
    def __init__(self, train_file):
        self.train_data = dict()
        self.user_item_history = dict()
        self.item2item_similary_matrix = dict()  # 文章-文章的共现矩阵
        self.item_count = dict()  # 文章被多少个用户阅读了
        self.get_data(train_file)

    def get_data(self, train_file):
        """
         从文件中读数据，生成训练数据集
        :param train_file: 训练文件
        :return: {person_id:{content_id:predict_score}}
        """
        with open(train_file, 'r', encoding='utf-8') as rf:
            for line in tqdm(rf.readlines()):
                user, score, item = line.strip().split(",")
                # 暂时做成 读取的数据放到内存中
                self.train_data.setdefault(user, {})
                self.user_item_history.setdefault(user, {})
                self.train_data[user][item] = int(score)
                self.user_item_history[user].append(item)

    def train(self):
        """
        基于 item 的协同过滤的训练模型，就是计算相似度
        :return: 相似矩阵 {content_id :{content_id: similary_score}}
        """
        for user, items in self.train_data.items():
            for i in items.keys():
                self.item_count.setdefault(i, 0)
                self.item_count[i] += 1

        # 因为需要提前计算 item_count 的数量，所以需要些两次 for，上面已经进行了一次
        for user, items in self.train_data.items():
            for i in items.keys():
                self.item2item_similary_matrix.setdefault(i, {})
                for j in items.keys():
                    if i == j:
                        continue
                    self.item2item_similary_matrix.setdefault(i, {})

                    # 计算的方式可根据不同的策略进行更改，这里只是乘积开根号取倒数
                    one_user_items_matrix = math.sqrt(self.item_count[i] * self.item_count[j])
                    self.item2item_similary_matrix[i][j] += 1 / one_user_items_matrix

        for _item in self.item2item_similary_matrix:
            self.item2item_similary_matrix[_item] = dict(sorted(self.item2item_similary_matrix[_item].items(),
                                                                key=lambda x: x[1], reversed=True)[0:30])

    def save(self):
        """
        训练的模型保存
        :return:
        """
        pass

    def cal_recall(self, user, topK=30):
        """
        计算召回,推荐给 user 对应的 item
        :param user:
        :param weight: 相似矩阵
        :param topK:取前 k 个
        :return:  推荐给 user 的 items list
        """

        rank = dict()  # 记录推荐给用户且去重后（已经读过）的商品，和感兴趣的程度
        action_item = self.train_data[user]

        for item, score in action_item.items():
            for j, wj in self.item2item_similary_matrix[item].items():
                if j in action_item.keys():
                    continue
                rank.setdefault(j, 0)
                rank[j] += score * wj / 10000  # 商品 j 与 商品item的相似度 * 商品item的兴趣得分，结果作为 user 对商品 j 的兴趣程度

        recall_ = list(dict(sorted(self.rank.items(), key=lambda x: x[1], reversed=True)[0:topK]))

        return recall_


if __name__ == '__main__':
    test_dict = {"name": {"name11": 1, "age11": 18}, "age": {"name22": 1, "age22": 18}}
    for it in test_dict:
        print(it)
