# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from database.base import VKFriendsDB
from database.models import Friends
import scrapy

class Kontach_2Pipelines(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vkfriends
        self.sql_db = VKFriendsDB('sqlite:///vkfriends.sqlite')
    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        db_item = Friends(spider=spider.name, friends=item.get('friends'), user=item.get('user'), deep=item.get('deep'))
        self.sql_db.add_friends(db_item)
        # print(item)
        return item

class KontachPipelines(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vkfriends
        self.sql_db = VKFriendsDB('sqlite:///vkfriends.sqlite')
    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        db_item = Friends(spider=spider.name, friends=item.get('friends'), user=item.get('user'), deep=item.get('deep'))
        self.sql_db.add_friends(db_item)
        # print(item)
        return item

