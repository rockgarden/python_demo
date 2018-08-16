# -*- coding: utf-8 -*-
# Created spider 'basic' using template 'basic' in module: properties.spiders.basic

# python3 urlparse 整合入 urllib

import scrapy

# 引入 PropertiesItem
from properties.items import PropertiesItem


class Basic0Spider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]

    # Start on a property page
    start_urls = (
        'http://web:9312/properties/property_000000.html',
    )

    def parse(self, response):
        item = PropertiesItem()
        item['title'] = response.xpath('//*[@itemprop="name"][1]/text()').extract()
        item['price'] = response.xpath('.//*[@itemprop="price"][1]/text()').re('[,.0-9]+').extract()
        item['description'] = response.xpath('//*[@itemprop="description"][1]/text()').extract()
        item['address'] = response.xpath('//*[@temtype="http://schema.org/Place"][1]/text()').extract()
        item['image_urls'] = response.xpath('//*[@itemprop="image"][1]/@src').extract()

        return item
