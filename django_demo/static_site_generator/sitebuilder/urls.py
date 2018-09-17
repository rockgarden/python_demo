from django.conf import settings
from django.conf.urls import url
from django.views import static

from .views import page

urlpatterns = (
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
    url(r'^$', page, name='homepage'),

    # 增加以下一行，以识别静态资源
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
)
