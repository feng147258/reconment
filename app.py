#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 6:49 PM
# @Author  : Yingjun Zhu
# @File    : app.py.py

from flask import Flask, jsonify, request
from web.service.pageData import PageData
from dataclean.dao.mysql_db import Mysql
from web.entity.user import UserId
from web.service.logData import LogData
from web.kafka_service import kafka_producter

app = Flask(__name__)

log_data = LogData()
page_data = PageData()


@app.route('/reconmend/get_rec_list', methods=['POST', 'GET'])
def bertsimer():
    if request.method == 'POST':
        page_size = request.get_json().get("pageSize")
        page_num = request\
            .get_json().get("pageNum")
        user_id = request.get_json().get("userId")
        types = request.get_json().get("types")

        try:
            # data = "page_size:" + str(page_size) + ",page_num:" + str(page_num) + ",user_id:" + str(user_id)
            data = page_data.get_page_data(page_size=page_size, page_num=page_num)
            return jsonify({"code": 0, "msg": "success", "data": data})
        except Exception as e:
            print(str(e))
            return jsonify({"code": 1000, "msg": "fail"})


@app.route('/reconmend/likes', methods=['POST', 'GET'])
def likes():
    if request.method == 'POST':
        title = request.get_json().get("title")
        content_id = request.get_json().get("contentId")
        user_id = request.get_json().get("userId")

    try:
        mysql = Mysql()
        session = mysql._DBSession()

        if session.query(UserId.id).filter(UserId.id == user_id).count() > 0:
            #
            if log_data.insert_log(user_id, content_id, title, "likes") and log_data.modify_articles_details("key", "likes"):
                kafka_producter.main("recommend", str.encode(str(content_id) + ":likes"))
                return jsonify({"code": 0, "msg": "success", "data": "喜欢成功"})
            else:
                return jsonify({"code": 1001, "msg": "success", "data": "喜欢失败"})
        else:
            return jsonify({"code": 1000, "msg": "success", "data": "用户不存在"})

    except Exception as e:
        print(str(e))
        return jsonify({"code": 1000, "msg": "fail"})


@app.route('/reconmend/read', methods=['POST', 'GET'])
def read():
    if request.method == 'POST':
        title = request.get_json().get("title")
        content_id = request.get_json().get("contentId")
        user_id = request.get_json().get("userId")

    try:
        mysql = Mysql()
        session = mysql._DBSession()

        if session.query(UserId.id).filter(UserId.id == user_id).count() > 0:
            if log_data.insert_log(user_id, content_id, title, "read") and log_data.modify_articles_details("key", "read"):

                return jsonify({"code": 0, "msg": "success", "data": "阅读陈宫"})
            else:
                return jsonify({"code": 1001, "msg": "success", "data": "阅读失败"})
        else:
            return jsonify({"code": 1000, "msg": "success", "data": "用户不存在"})

    except Exception as e:
        print(str(e))
        return jsonify({"code": 1000, "msg": "fail"})


@app.route('/reconmend/collections', methods=['POST', 'GET'])
def collections():
    if request.method == 'POST':
        title = request.get_json().get("title")
        content_id = request.get_json().get("contentId")
        user_id = request.get_json().get("userId")

    try:
        mysql = Mysql()
        session = mysql._DBSession()

        if session.query(UserId.id).filter(UserId.id == user_id).count() > 0:
            if log_data.insert_log(user_id, content_id, title, "collections") and log_data.modify_articles_details("key", "collections"):

                return jsonify({"code": 0, "msg": "success", "data": "收藏成功"})
            else:
                return jsonify({"code": 1001, "msg": "success", "data": "收藏失败"})
        else:
            return jsonify({"code": 1000, "msg": "success", "data": "接口操作出现问题"})

    except Exception as e:
        print(str(e))
        return jsonify({"code": 1000, "msg": "fail"})


def register():
    pass


def login():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=False, port=8080)
