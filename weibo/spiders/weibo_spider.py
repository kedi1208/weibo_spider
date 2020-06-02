# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from weibo.items import WeiboItem
import time
import uuid
# time.strftime('%Y-%m-%d %H:%M', time.localtime())

class WeiboSpiderSpider(scrapy.Spider):
    name = 'weibo_spider'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']

    def parse(self, response):
        if response:
            in_time = time.strftime('%Y-%m-%d %H:%M', time.localtime())
            bs = BeautifulSoup(response.text, 'html.parser')
            realtimehot = bs.find(id="pl_top_realtimehot")
            tbody = realtimehot.find("tbody")
            lines = tbody.find_all("tr")
            # tops = []
            for line in lines:
                # topn = {}
                hotItem = WeiboItem()
                if line.find('td',class_="td-01 ranktop") is not None:
                    hotItem["topic_rank"] = line.find('td',class_="td-01 ranktop").string
                    hotItem["topic_name"] = line.find('td',class_="td-02").a.get_text()
                    hotItem["topic_hot"] = line.find('td',class_="td-02").span.get_text()
                    hotItem["hot_type"] = line.find('td',class_="td-03").string if line.find('td',class_="td-03").string is not None else ''
                    hotItem["in_time"] = in_time
                    hotItem["topic_id"] = "".join(str(uuid.uuid4()).split("-"))
                    yield hotItem
                    #print(hotItem["topic_name"])
                    # topn["rank"] = line.find('td',class_="td-01 ranktop").string
                    # topn["topic"] = line.find('td',class_="td-02").a.get_text()
                    # topn["hot"] = line.find('td',class_="td-02").span.get_text()
                    # topn["hottype"] = line.find('td',class_="td-03").string if line.find('td',class_="td-03").string is not None else ''
                    # tops.append(dict(topn))
                    # topn.clear()
                    # tops.append(dict(hotItem))
            # yield tops

