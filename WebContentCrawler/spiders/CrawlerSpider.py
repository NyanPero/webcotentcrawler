# -*- coding: utf-8 -*-
import scrapy
from ..items import WebcontentcrawlerItem
from scrapy_splash import SplashRequest
import datetime



class CrawlerSpider(scrapy.Spider):
    name = 'Crawler'
    start_urls = []
    
    def __init__(self, url_list=[], user_agent=None, *args, **kwargs):
        super(CrawlerSpider, self).__init__(*args, **kwargs)
        self.start_urls = url_list
        self.user_agent = user_agent

    
    def start_requests(self):
        splash_args = {
            'html': 1,
            'jpeg': 1,
            'width': 640,
            'height': 480,
            'wait': 10,
            'har': 1,
            'iframe': 1,
            'script': 1,
            'console': 1,
            'history': 1,
            'request_body': 1,
            'response_body': 1,
            'render_all': 1
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.json', args=splash_args)

    def parse(self, response):
        item = WebcontentcrawlerItem()
        item['title'] = response.css('title::text').getall()
        item['screenshot'] = response.data['jpeg']
        item['redirected_url'] = response.url
        item['original_url'] = response.data['har']['log']['entries'][0]['request']['url']
        now = datetime.datetime.now()
        item['crawled_datetime'] = now.strftime("%Y-%m-%dT%H:%M:%S")
        yield item
