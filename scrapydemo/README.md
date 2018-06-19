# scrapy demo
http://sangaline.com/post/advanced-web-scraping-tutorial/

## crawl常规返爬技术应对
1. User agent 过滤
    Scrapy将其标识为“Scrapy / 1.3.3（+ http：//scrapy.org）”，某些服务器可能会阻止它或者甚至只是将有限数量的User Agent列入白名单。 
    
    在`settings.py`指定
    
    
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

2. 爬虫访问表现得更像人类的操作

    降低请求速率(原理上借助[AutoThrottle](https://link.jianshu.com/?t=https://doc.scrapy.org/en/latest/topics/autothrottle.html))，在settings.py
    
    
    CONCURRENT_REQUESTS = 1
    DOWNLOAD_DELAY = 5

3. 模糊的JavaScript重定向

    页面中有一些JavaScript代码用于构造一个特殊的重定向URL与设置浏览器cookies, 一般返回302重定向code.
    
    一般在定制(自定义)的redirect middleware（重定向中间件）里解决 302 问题.
    
    启用我们的新中间件，要在`settings.py`添加如下内容:
    
    
    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
        'zipru_scraper.middlewares.ThreatDefenceRedirectMiddleware': 600,
    }
    
4. 验证码

    [anti-captcha](https://anti-captcha.com/):处理验证码的API。
    
    简单验证码可以用OCR来处理，如使用pytesseract做字符识别。
    
5. 请求头一致性检验

    通过一个加密的访问Cookie包含了完整的原始访问请求头的哈希值，如果两次请求头不匹配，将触发威胁防御机制。
    这里的意图可能是防止某人直接将浏览器的cookies复制到爬虫中。
    
	可在`settings.py`明确指定我们的请求头：


    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': USER_AGENT,
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,*',
    }


## 常用的辅助库
- [requests](http://www.python-requests.org/en/master/)
- [BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/)
- [selenium](https://pypi.org/project/selenium/)
- [execJS](https://pypi.org/project/PyExecJS/)
- [pytesseract](https://pypi.org/project/pytesseract/):基于Tesseract-OCR引擎的封装

- [rsa](https://pypi.org/project/rsa/)
- [PIL](https://pypi.org/project/Pillow/)

### dryscrape 安装
先装`webkit-server`再装`dryscrape`
- [webkit-server](https://pypi.org/project/webkit-server/):headless webkit 无头webkit服务端
- [dryscrape](https://pypi.org/project/dryscrape/)

若无效参见 https://github.com/niklasb/dryscrape/issues/45, 修改`requirements.txt`:

    -e git+https://github.com/niklasb/webkit-server.git#egg=webkit-server
    lxml
    git+git://github.com/niklasb/webkit-server.git
    xvfbwrapper
    
http://dryscrape.readthedocs.io/en/latest/installation.html