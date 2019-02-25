# -*- coding: utf-8 -*-
import scrapy
from shenshe.items import ArticleItem


class ShensheSpider(scrapy.Spider):
    name = 'Shenshe'
    allowed_domains = ['www.liuli.in']
    start_urls = ['https://www.liuli.in/wp']

    def parse(self, response):
        articles = response.css('#content article')
        for article in articles:
            url = article.css('header h1 a::attr(href)').extract_first()
            if url:
                img_url = article.css('.entry-content img::attr(src)').extract_first()
                yield scrapy.Request(url=url, callback=self.parse_item, meta={'img_url': img_url})

        next = response.xpath('//div[@id="wp_page_numbers"]/ul/li[last()]/a/@href').extract_first()
        if next:
            yield scrapy.Request(url=next, callback=self.parse)

    def parse_item(self, response):
        item = ArticleItem()
        item['title'] = response.css('#content article header > h1::text').extract_first()
        item['author'] = response.css('#content article header > div .by-author a::text').extract_first()
        item['datetime'] = response.css('#content article header > div > a > time::text').extract_first()
        # item['content'] = response.css('#content article .entry-content::text').extract_first()
        item['magnet'] = 'magnet:?xt=urn:btih:'+response.xpath('//div[@id="content"]//div[@class="entry-content"]//text()').re_first('[0-9|a-z|A-Z]{40}')
        item['comment_source'] = response.css('#comments-title span::text').extract_first()
        item['comments'] = response.xpath('//h2[@id="comments-title"]/text()').re_first('(\d+)')
        item['score'] = response.xpath('//div[@id="content"]/article/div[@class="entry-header"]'
                                       '/div[@class="post-ratings"]/strong[2]/text()').extract_first()
        item['score_nums'] = response.xpath('//div[@id="content"]/article/div[@class="entry-header"]'
                                            '/div[@class="post-ratings"]/strong[1]/text()').extract_first()
        item['img_url'] = response.meta.get('img_url')
        yield item
