# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class WeiboSpiderSpider(scrapy.Spider):
    name = 'weibo_spider'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']

    def parse(self, response):
        if response:
            bs = BeautifulSoup(response.text, 'html.parser')
            realtimehot = bs.find(id="pl_top_realtimehot")
            tbody = realtimehot.find("tbody")
            lines = tbody.find_all("tr")
            tops = []
            for line in lines:
                topn = {}
                if line.find('td',class_="td-01 ranktop") is not None:
                    topn["rank"] = line.find('td',class_="td-01 ranktop").string
                    topn["topic"] = line.find('td',class_="td-02").a.get_text()
                    topn["hot"] = line.find('td',class_="td-02").span.get_text()
                    topn["hottype"] = line.find('td',class_="td-03").string if line.find('td',class_="td-03").string is not None else ''
                    tops.append(dict(topn))
                    topn.clear()
            print(tops)
