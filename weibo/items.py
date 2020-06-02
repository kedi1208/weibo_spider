# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic_id = scrapy.Field()
    topic_name = scrapy.Field()
    topic_rank = scrapy.Field()
    topic_hot = scrapy.Field()
    hot_type = scrapy.Field()
    in_time = scrapy.Field()
