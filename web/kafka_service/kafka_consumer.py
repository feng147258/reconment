#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 2:49 PM
# @Author  : Yingjun Zhu
# @File    : kafka_consumer.py

from kafka import KafkaConsumer
from kafka.structs import TopicPartition
import time

class Consumer(object):
    """
    kafka的消费者
    """
    def __init__(self):
        self.consumer = KafkaConsumer(
            group_id="test",
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            bootstrap_servers=["127.0.0.1:9092"]
        )

    def consumer_data(self, topic, partition):
        my_partition = TopicPartition(topic=topic, partition=partition)
        self.consumer.assign([my_partition])
        print(f"consumer start partition :{self.consumer.position(my_partition)}")

        try:
            while True:
                poll_num = self.consumer.poll(timeout_ms=1000, max_records=5)
                if poll_num == {}:
                    print("empty")
                    exit(1)
                for key, record in poll_num.items():
                    for message in record:
                        #数据的处理，用到
                        print(f"topic:{message.topic} partition:{message.partition} offset:{message.offset} "
                              f"key={message.key} value={message.value}")

                try:
                    self.consumer.commit_async()
                    # time.sleep(2)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

        finally:
            try:
                self.consumer.commit()
            finally:
                self.consumer.close()

if __name__ == '__main__':
    topic = 'recommend'
    partition = 0
    my_consumer = Consumer()
    my_consumer.consumer_data(topic=topic,partition=partition)

