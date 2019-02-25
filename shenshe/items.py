# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    author = scrapy.Field()
    title = scrapy.Field()
    magnet = scrapy.Field()
    datetime = scrapy.Field()
    comments = scrapy.Field()
    comment_source = scrapy.Field()
    score = scrapy.Field()
    score_nums = scrapy.Field()
    img_url = scrapy.Field()


class FaceImgItem(scrapy.Item):
    img_url = scrapy.Field()