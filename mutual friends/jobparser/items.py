# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

class Kontach_2Item(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Spider
    friends = scrapy.Field()
    user = scrapy.Field()
    deep = scrapy.Field()

class KontachItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Spider
    friends = scrapy.Field()
    user = scrapy.Field()
    deep = scrapy.Field()