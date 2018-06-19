import logging
import os
import sys
import tempfile
import time

logger = logging.getLogger(__name__)

import dryscrape
import pytesseract
from PIL import Image

from scrapy.downloadermiddlewares.redirect import RedirectMiddleware


class ThreatDefenceRedirectMiddleware(RedirectMiddleware):

    def _redirect(self, redirected, request, spider, reason):
        """
        会被process_response(request, response, spider)方法调用
        :param redirected:
        :param request:
        :param spider:
        :param reason:
        :return:
        """
        # 如果没有特殊的防范性重定向那就正常工作
        if not self.is_threat_defense_url(redirected.url):
            return super()._redirect(redirected, request, spider, reason)

        logger.debug(f'Threat defense triggered for {request.url}')
        request.cookies = self.bypass_threat_defense(redirected.url)
        request.dont_filter = True  # 防止原始链接被标记为重复链接
        return request

    def is_threat_defense_url(self, url):
        """
        判断是否为 hreat_defense 页面
        :param url:
        :return:
        """
        return '://demo.com/threat_defense.xxx' in url

    def __init__(self, settings):
        """
        初始化一个 dryscrape 会话：
            会话当作一个浏览器标签，它会做所有浏览器通常所做的事（如获取外部资源，获取脚本）。
            我们可以在选项卡中导航到新的URL，点击按钮，输入文本以及做其它各类事务。
        注：
        Scrapy支持请求和项目处理的并发，但响应的处理是单线程的, 所以可以使用这个单独的 dryscrape 会话，而不用担心线程安全。
        :param settings:
        """
        super().__init__(settings)

        # start xvfb to support headless scraping
        # 用 dryscrape 构造无头 webkit 实例
        if 'linux' in sys.platform:
            dryscrape.start_xvfb()

        self.dryscrape_session = dryscrape.Session(base_url='http://demo.com')

    def bypass_threat_defense(self, url=None):
        """
        返回访问cookies，使得我们可以刷新原始请求的cookies，而重新处理原始请求
        :param url:
        :return:
        """
        # 有确实的url则访问
        if url:
            self.dryscrape_session.visit(url)

        # 如果有验证码则处理
        captcha_images = self.dryscrape_session.css('img[src *= captcha]')
        if len(captcha_images) > 0:
            return self.solve_captcha(captcha_images[0])

        # 点击可能存在的重试链接
        retry_links = self.dryscrape_session.css('a[href *= threat_defense]')
        if len(retry_links) > 0:
            return self.bypass_threat_defense(retry_links[0].get_attr('href'))

        # 否则的话，我们是在一个重定向页面上，等待重定向后再次尝试
        self.wait_for_redirect()
        return self.bypass_threat_defense()

    def wait_for_redirect(self, url=None, wait=0.1, timeout=10):
        url = url or self.dryscrape_session.url()
        for i in range(int(timeout // wait)):
            time.sleep(wait)
            # 如果url发生变化则返回
            if self.dryscrape_session.url() != url:
                return self.dryscrape_session.url()
        logger.error(f'Maybe {self.dryscrape_session.url()} isn\'t a redirect URL?')
        raise Exception('Timed out on the demo redirect page.')

    def solve_captcha(self, img, width=1280, height=800):
        """
        处理验证码。
        :param img:
        :param width:
        :param height:
        :return:
        """
        # 对当前页面截图
        self.dryscrape_session.set_viewport_size(width, height)
        filename = tempfile.mktemp('.png')
        self.dryscrape_session.render(filename, width, height)

        # 注入javascript代码来找到验证码图片的边界
        js = 'document.querySelector("img[src *= captcha]").getBoundingClientRect()'
        rect = self.dryscrape_session.eval_script(js)
        box = (int(rect['left']), int(rect['top']), int(rect['right']), int(rect['bottom']))

        # 解决截图中的验证码
        image = Image.open(filename)
        os.unlink(filename)
        captcha_image = image.crop(box)
        captcha = pytesseract.image_to_string(captcha_image)
        logger.debug(f'Solved the demo captcha: "{captcha}"')

        # 提交验证码结果
        input = self.dryscrape_session.xpath('//input[@id = "solve_string"]')[0]
        input.set(captcha)
        button = self.dryscrape_session.xpath('//button[@id = "button_submit"]')[0]
        url = self.dryscrape_session.url()
        button.click()

        # 如果我们被重定向到一个防御的URL，重试
        if self.is_threat_defense_url(self.wait_for_redirect(url)):
            return self.bypass_threat_defense()

        # 否则就可以返回当前的cookies构成的字典
        cookies = {}
        for cookie_string in self.dryscrape_session.cookies():
            if 'domain=demo.com' in cookie_string:
                key, value = cookie_string.split(';')[0].split('=')
                cookies[key] = value
        return cookies
