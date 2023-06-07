import scrapy


class HualongSpider(scrapy.Spider):
    name = "hualong"
    allowed_domains = ["www.58hualong.cn"]
    start_urls = ["https://www.58hualong.cn/meishi/index_2.html"]

    def parse(self, response):
        # /html/body/div[3]/div[2]/div[3]/ul/li/a/@title
        for item in response.xpath("/html/body/div[3]/div[2]/div[3]/ul/li/a"):
            title = item.xpath("./@title").get()
            yield {"title": title}

