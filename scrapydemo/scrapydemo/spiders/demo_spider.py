import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    start_urls = ['http://demo.com']

    def parse(self, response):
        # 从页面中取出页码里包含的链接
        for page_url in response.css('a[title ~= page]::attr(href)').extract():
            page_url = response.urljoin(page_url)
            # 将解析出的href里的链接自动判断补全
            yield scrapy.Request(url=page_url, callback=self.parse)
            # 由解析出的url生成新的请求对象

            # 提取内容信息
            for tr in response.css('table.lista2t tr.lista2'):
                tds = tr.css('td')
                link = tds[1].css('a')[0]
                yield {
                    'title': link.css('::attr(title)').extract_first(),
                    'url': response.urljoin(link.css('::attr(href)').extract_first()),
                    'date': tds[2].css('::text').extract_first(),
                    'size': tds[3].css('::text').extract_first(),
                    'seeders': int(tds[4].css('::text').extract_first()),
                    'leechers': int(tds[5].css('::text').extract_first()),
                    'uploader': tds[7].css('::text').extract_first(),
                }
