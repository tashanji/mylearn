# -*- coding: utf-8 -*-
import scrapy


class LiveSpider(scrapy.Spider):
    name = 'live'
    allowed_domains = ['wallstreetcn.com']
    start_urls = ['https://wallstreetcn.com/live/global/']

    def parse(self, response):
        first_pane=response.xpath('/html/body//div[@class="wscn-tab-pane"]')[0]
        for s in first_pane.xpath('//div[@class="live-item score-1"]'):
            yield {
                'time': s.xpath('//div[@class="live-item__time"]/span[@class="live-item__time__text"]/text()').extract_first()
#                'time': s.xpath('//div[@class="live-item__time"]/span[@class="live-item__time__text"]').extract_first()
            }

