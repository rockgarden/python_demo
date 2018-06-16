# -*- coding: utf-8 -*-
import random
import re

import scrapy


# TODO: https://blog.csdn.net/real_Rickys/article/details/79780650

# from lego import UserAgent

class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['baidu.com', 'eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    def parse(self, response):
        ua = random.choice(self.user_agent_list)  # 随机抽取User-Agent
        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Referer': 'https://gupiao.baidu.com/',
            'User-Agent': ua
        }  # 构造请求头

        # rh = UserAgent.random_header()

        for href in response.css('a::attr(href)').extract()[10:200]:  # 用CSS Selector提取信息
            try:
                stock = re.findall(r'[s][hz]\d{6}', href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'  # 百度股票对应的链接
                yield scrapy.Request(url, callback=self.parse_stock, headers=headers)  # callback给出处理这个url对应响应的处理函数
            except:
                continue

    @staticmethod
    def parse_stock(response):
        info_dict = {}
        stock_info = response.css('.stock-bets')
        # print(stock_info)
        name = stock_info.css('.bets-name').extract()[0]
        # print(name)
        key_list = stock_info.css('dt').extract()
        # print(key_list)
        value_list = stock_info.css('dd').extract()
        # print(value_list)
        for i in range(len(key_list)):
            key = re.findall(r'>.*</dt>', key_list[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', value_list[i])[0][0:-5]
            except:
                val = '--'
            info_dict[key] = val

        info_dict.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + re.findall('\>.*<', name)[0][1:-1]})
        yield info_dict
