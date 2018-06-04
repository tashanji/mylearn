import scrapy

class FutuSpider(scrapy.Spider):
    name = "futu"
    allowed_domains = ["futunn.com"]
    start_urls = [
        "https://news.futunn.com/main",
    ]

    def parse(self, response):
        for s in response.xpath('/html/body//ul[@id="news-list-container"]//a[@class="news-link"]'):
            yield {
                'title': s.xpath('.//h3[@class="news-title"]/text()').extract(),
                'url':s.xpath("./@href").extract(),
                'time':s.xpath('.//span[@class="news-time"]/text()').extract()
            }
