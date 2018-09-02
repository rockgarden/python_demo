# -*- coding: utf-8 -*-
# Created spider 'basic' using template 'basic' in module: properties.spiders.basic

import datetime
import socket
# python3 urlparse 整合入 urllib
from urllib.parse import urlparse

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

# 引入 PropertiesItem
from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]

    # Start on a property page
    start_urls = (
        'http://web:9312/properties/property_000000.html',
    )

    def parse(self, response):
        # contract：用于运行 scrapy check 检查约定(contract)是否满足
        """ This function parses a property page.
        @url http://web:9312/properties/property_000000.html
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date
        """

        # Create the Loader using the response
        # 实例化工具类 ItemLoader(项目加载器) 填充 item (字段)项目
        # 项目加载器通过自动执行一些常见任务（例如在分配原始提取数据之前解析原始提取数据），并提供API，用于从抓取过程中填充它们。
        # Items提供了抓取数据的容器，而Loaders提供了填充该容器的机制。
        # 这里的 item 实例化 PropertiesItem 子类
        l = ItemLoader(item=PropertiesItem(), response=response)

        # Load fields using XPath expressions
        # 并用处理器 MapCompose / Join 处理数据
        # python 2 str => unicode
        l.add_xpath('title', '//*[@itemprop="name"][1]/text()',
                    MapCompose(str.strip, str.title))
        l.add_xpath('price', './/*[@itemprop="price"][1]/text()',
                    MapCompose(lambda i: i.replace(',', ''), float),
                    re='[,.0-9]+')  # 将字符串转换为数值, 并忽略','字符
        l.add_xpath('description', '//*[@itemprop="description"][1]/text()',
                    MapCompose(str.strip), Join())  # 多结果连接
        l.add_xpath('address',
                    '//*[@itemtype="http://schema.org/Place"][1]/text()',
                    MapCompose(str.strip))
        l.add_xpath('image_urls', '//*[@itemprop="image"][1]/@src',
                    MapCompose(lambda i: urlparse.urljoin(response.url, i)))  # 以 response.url 为基础将生成绝对路径

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        return l.load_item()
