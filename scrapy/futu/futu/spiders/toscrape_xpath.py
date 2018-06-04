# -*- coding: utf-8 -*-
import scrapy


class ToscrapeXpathSpider(scrapy.Spider):
    name = 'toscrape-xpath'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://www.toscrape.com/']

    def parse(self, response):
        pass
