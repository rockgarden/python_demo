# 自定义管理命令-用于生成网页
# run command:
# 生成单个所有页面
# $ python3 prototypes.py build
# 生成单个page index.html
# $ python3 prototypes.py build index
# $ cd _build
# $ python3 -m http.server 9000

# 若在build page 时出现：
# TemplateSyntaxError Invalid block tag: 'else', expected 'endif', Did you forget to register or load this tag?
# 一般是 html 代码格式异常.

import os
import shutil

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.test.client import Client
from django.urls import reverse


def get_pages():
    for name in os.listdir(settings.SITE_PAGES_DIRECTORY):
        if name.endswith('.html'):
            yield name[:-5]


class Command(BaseCommand):
    help = 'Build static site output.'
    leave_locale_alone = True

    def add_arguments(self, parser):
        """
        检查是否有任何参数传递给命令(指定生成哪个page), 一次可以传递多个参数.
        :param parser:
        """
        parser.add_argument('args', nargs='*')

    def handle(self, *args, **options):
        """Request pages and build output."""
        settings.DEBUG = False
        settings.COMPRESS_ENABLED = True  # 启动表态压缩
        if args:  # 处理传入由命令带入的参数.
            pages = args
            available = list(get_pages())
            invalid = []
            for page in pages:
                if page not in available:
                    invalid.append(page)
            if invalid:
                # 如果传递的 page 名称不存在, 则会引发错误.
                msg = 'Invalid pages: {}'.format(', '.join(invalid))
                raise CommandError(msg)
        else:
            pages = get_pages()

        # 检查输出目录是否存在，如果存在，则将其删除以创建干净版本。
        if os.path.exists(settings.SITE_OUTPUT_DIRECTORY):
            shutil.rmtree(settings.SITE_OUTPUT_DIRECTORY)
        os.mkdir(settings.SITE_OUTPUT_DIRECTORY)
        os.makedirs(settings.STATIC_ROOT, exist_ok=True)

        # 使用 call_command 实用程序运行 collecstatic 命令将所有站点静态资源复制到STATIC_ROOT中，
        # 该STATIC_ROOT配置为在SITE_OUTPUT_DIRECTORY内。
        call_command('collectstatic', interactive=False, clear=True, verbosity=0)

        # 压缩 templates 中带 'compress' 标记的内容, 并输出到 /static/CACHE 目录下.
        call_command('compress', traceback=False, force=True)

        client = Client()

        # 遍历 pages 目录并收集位于那里的所有.html文件。
        for page in pages:
            url = reverse('page', kwargs={'slug': page})
            response = client.get(url)
            if page == 'index':
                output_dir = settings.SITE_OUTPUT_DIRECTORY
            else:
                output_dir = os.path.join(settings.SITE_OUTPUT_DIRECTORY, page)
                if not os.path.exists(output_dir):  # 处理目录已存在的情况
                    os.makedirs(output_dir)

            # 模板呈现为静态内容的位置。
            # 使用Django测试客户端来模仿抓取网站页面并将呈现的内容写入SITE_OUTPUT_DIRECTORY。
            with open(os.path.join(output_dir, 'index.html'), 'wb') as f:
                f.write(response.content)
