# run command:
# $ cd ./hooksasync
# $ python3 -m scrapy crawl test

from scrapy.item import Item, Field
from scrapy.spider import Spider


class HooksasyncItem(Item):
    name = Field()


class TestSpider(Spider):
    name = "test"
    allowed_domains = ["example.com"]
    start_urls = ('http://www.example.com',)

    def parse(self, response):
        for i in range(2):
            item = HooksasyncItem()
            item['name'] = "Hello %d" % i
            yield item
        raise Exception("dead")
