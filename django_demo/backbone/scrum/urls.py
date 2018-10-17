from django.conf.urls import include, url
# 使用通用TemplateView
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from board.urls import router

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),

    # 加入新的模式来将服务器根节点渲染成board/index.html
    url(r'^$', TemplateView.as_view(template_name='board/index.html')),
]