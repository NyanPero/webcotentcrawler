# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcontentcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    original_url = scrapy.Field()
    redirected_url = scrapy.Field()
    screenshot = scrapy.Field()
    crawled_datetime = scrapy.Field()