#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 2:30 PM
# @Author  : zhuyingjun
# @File    : tf_idf.py

import os, re
import jieba
import jieba.analyse
import jieba.posseg as pseg


class Segment(object):
    def __init__(self, stopword_files, userdict_files=[], jieba_tmp_dir=None):
        if jieba_tmp_dir:
            jieba.dt.tmp_dir = jieba_tmp_dir
            if not os.path.exists(jieba_tmp_dir):
                os.makedirs(jieba_tmp_dir)
        self.stopwords = set()  # 因为停用词需要去重，直接使用了 set 收集

        for stopword_file in stopword_files:
            with open(stopword_file, "r", encoding="utf-8") as rf:
                for row in rf.relines():
                    word = row.strip()
                    if len(word) > 0:
                        self.stopwords.add(word)

        for userdict_file in userdict_files:
            # 加载用户自定义词典
            jieba.load_userdict(userdict_file)

    def cut(self, text):
        '''
        :param text: 需要处理的文本
        :return:  文本分词、去停用词后的 list形式
        '''
        word_list = []
        text.replace('\n', '').replace('\u3000', '').replace('\u00A0', '')
        text = re.sub('[a-zA-Z0-9.。:：,，]', '', text)
        words = pseg.cut(text)

        for word in words:
            print(word.word, word.flag)
            word = word.strip()
            if word in self.stopwords or len(word) == 0:
                continue
            word_list.append(word)
        return word_list

    def extract_keyword(self,text,algorithm ='tf_idf',use_pos=True):
        '''
        :param text:
        :param algorithm:
        :param use_pos:
        :return: 根据 text 提取到的关键词
        '''
        text = re.sub('[a-zA-Z0-9.。:：,，]', '', text)
        if use_pos:
            allow_pos = ('n','nr','ns','vn','v')

        if algorithm =='tf_idf':
            tags = jieba.analyse.extract_tags(text, withWeight=False)
            return tags
        elif algorithm == "text_rank":
            text_rank = jieba.analyse.textrank(text,withWeight=False,allowPOS=allow_pos)
            return text_rank

if __name__ == '__main__':
    seg =Segment(stopword_files=[],userdict_files=[])
    text = "今天天气很好呀"
    tag_tf_idf = seg.extract_keyword(text,algorithm ='tf_idf',use_pos=True)[:25]
    tag_text_rank = seg.extract_keyword(text,algorithm= "text_rank",use_pos=True)[:25]
    print(tag_tf_idf)
    print(tag_text_rank)
    print(set(tag_text_rank) & set(tag_tf_idf))

