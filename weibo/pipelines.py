# -*- coding: utf-8 -*-
# import pymongo
# import pymongo.errors as mongoError
import pymysql
# from weibo.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection,mongo_host_uri
from weibo import settings
import uuid

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class WeiboPipeline:
    def __init__(self):
        # mongo conn
        # self.dbname = mongo_db_name
        # self.collection_name = mongo_db_collection
        # self.mongo_uri = mongo_host_uri
        
        # mysql conn
        self.host = settings.mysql_host
        self.port = settings.mysql_port
        self.user = settings.mysql_user
        self.passwd = settings.mysql_passwd
        self.db_name = settings.mysql_db_name

    def open_spider(self, spider):
        # mongo conn
        # self.client = pymongo.MongoClient(self.mongo_uri)
        # self.db = self.client[self.dbname]
        
        # mysql conn
        self.db = pymysql.connect(host=self.host,
                                port=int(self.port),
                                user=self.user,
                                password=self.passwd,
                                database=self.db_name,
                                charset="utf8")
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        # mongo conn
        # self.client.close()

        # mysql conn
        self.cursor.close()
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)  # item 从spider yeld过来的
        # mongo conn
        # try:
        #     self.db[self.collection_name].insert_one(data) # 插入数据库
        # except mongoError.AutoReconnect:
        #     print("=====================触发 AutoReconnect 异常。=====================")

        # mysql conn
        try:
            sql = 'INSERT INTO weibohot (id,topic_name,topic_rank,topic_hot,in_time,hot_type) VALUES \
                ("{5}","{0}", {1}, {2}, "{3}", "{4}" )'.format(data["topic_name"], 
                int(data["topic_rank"]), int(data["topic_hot"]), data["in_time"], data["hot_type"], data["topic_id"])
            # print(sql)
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e.args)
            self.db.rollback()
        # 在 close_spider 中关闭数据库
        # finally:
        #     self.cursor.close()
        #     self.db.close()
        return item
