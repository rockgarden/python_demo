# run command:
# $ pip3 install django_compressor
# $ python3 prototypes.py runserver

import os
import sys

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1, localhost').split(',')

settings.configure(
    DEBUG=False,
    SECRET_KEY='b0mqvak1p2sqm6p#+8o8fyxf+ox(le)8&jh_5^sxa!=7!+wxj0',
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
        'compressor',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.static',
                ],
            },
        },
    ),

    # 设置静态资源路径
    STATIC_URL='/static/',
    STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'),  # 启用存放在_build目录下的静态内容.

    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),  # 此设置配置了, 文件生成命令完成后, 生成的静态文件所存放的输出目录。

    STATICFILES_FINDERS=(
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ),

    # TODO: 生成哈希文件名的
    # 当 DEBUG=False (并且 build.py handle() 方法中的 setting.DEBUG = False)时django会生成哈希文件名的静态文件.
    # 见 _build/static/CACHE 目录.
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.CachedStaticFilesStorage',
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
