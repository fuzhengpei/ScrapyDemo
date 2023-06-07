import scrapy


class CnblogSpider(scrapy.Spider):
    name = "cnblog"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]

    def parse(self, response):
        pass
