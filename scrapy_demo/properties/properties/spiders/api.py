import datetime
import json
import socket
from urllib.parse import urljoin

import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

from properties.items import PropertiesItem


class ApiSpider(scrapy.Spider):
    name = 'api'
    allowed_domains = ["web"]

    # Start on the first index page
    start_urls = (
        'http://web:9312/properties/api.json',
    )

    # Format the URLs based on the API call response
    def parse(self, response):
        base_url = "http://web:9312/properties/"
        js = json.loads(response.body)
        for item in js:
            id = item["id"]
            title = item["title"]
            url = base_url + "property_%06d.html" % id
            # 通过meta字典传递参数
            yield Request(url, meta={"title": title}, callback=self.parse_item)

    def parse_item(self, response):
        """ This function parses a property page.

        @url http://web:9312/properties/property_000000.html
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date
        """

        # Create the loader using the response
        l = ItemLoader(item=PropertiesItem(), response=response)

        # 使用add_value()方法获取response.meta
        l.add_value('title', response.meta['title'],
                    MapCompose(str.strip, str.title))

        # Load fields using XPath expressions
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
