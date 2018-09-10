# -*- coding: utf-8 -*-
# run command:
# $ scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=90 -L DEBUG

import datetime
import socket
from urllib.parse import urljoin

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from scrapy.spiders import CrawlSpider, Rule

from properties.items import PropertiesItem


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['web']

    # Start on the first index page
    start_urls = (
        'http://web:9312/properties/index_00000.html',
    )

    # Rules for horizontal and vertical crawling
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # LinkExtractor 抽取链接的函数.
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"next")]')),
        Rule(LinkExtractor(restrict_xpaths='//*[@itemprop="url"]'), callback='parse_item'),
    )

    def parse_item(self, response):
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
        l.add_value('server', (lambda i: i + ' (' + socket.gethostbyname(i) +
                                         ')')(socket.gethostname()))
        l.add_value('date', datetime.datetime.now())

        return l.load_item()
