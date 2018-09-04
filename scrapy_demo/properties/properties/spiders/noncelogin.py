import datetime
import socket
from urllib.parse import urljoin

from scrapy.http import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from scrapy.spiders import CrawlSpider, Rule

from properties.items import PropertiesItem


class NonceLoginSpider(CrawlSpider):
    name = 'noncelogin'
    allowed_domains = ["web"]

    # Start on the welcome page
    # 获取 nonce info
    def start_requests(self):
        return [
            Request(
                "http://web:9312/dynamic/nonce",
                callback=self.parse_welcome)
        ]

    # Post welcome page's first form with the given user/pass
    def parse_welcome(self, response):
        return FormRequest.from_response(
            response,
            formdata={"user": "user", "pass": "pass"}
        )

    # Rules for horizontal and vertical crawling
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"next")]')),
        Rule(LinkExtractor(restrict_xpaths='//*[@itemprop="url"]'),
             callback='parse_item')
    )

    def parse_item(self, response):
        """ This function parses a property page.

        @url http://web:9312/properties/property_000000.html
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date
        """

        # Create the loader using the response
        l = ItemLoader(item=PropertiesItem(), response=response)

        # Load fields using XPath expressions
        l.add_xpath('title', '//*[@itemprop="name"][1]/text()',
                    MapCompose(str.strip, str.title))
        l.add_xpath('price', './/*[@itemprop="price"][1]/text()',
                    MapCompose(lambda i: i.replace(',', ''), float),
                    re='[,.0-9]+')
        l.add_xpath('description', '//*[@itemprop="description"][1]/text()',
                    MapCompose(str.strip), Join())
        l.add_xpath('address',
                    '//*[@itemtype="http://schema.org/Place"][1]/text()',
                    MapCompose(str.strip))
        l.add_xpath('image_urls', '//*[@itemprop="image"][1]/@src',
                    MapCompose(lambda i: urljoin(response.url, i)))

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        return l.load_item()
