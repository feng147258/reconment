#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 2:27 PM
# @Author  : Yingjun Zhu
# @File    : kafka_producter.py

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors


def main(topic,msg):
    producer = KafkaProducer(bootstrap_servers=["127.0.0.1:9092"])

    for i in range(5):
        msg = "msg" + str(i)
        future = producer.send(topic,  str.encode(msg))

        try:
            record_metadata = future.get(timeout=10)
            print(record_metadata)

        except kafka_errors as e:
            print(e)


if __name__ == '__main__':
    main()
