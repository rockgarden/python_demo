from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters

from .models import Sprint, Task
from .my_filters import SprintFilter, TaskFilter
from .serializers import SprintSerializer, TaskSerializer, UserSerializer

# Create your views here.

User = get_user_model()


class DefaultsMixin(object):
    """
    DefaultsMixin将是API视图类的基类之, 实现 authentication
    Default settings for view authentication, permissions, filtering
     and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    # 存放需要可用filters的列表
    filter_backends = (
        filters.BaseFilterBackend,
        # filters.DjangoFilterBackend,
        # module 'rest_framework.filters' has no attribute 'DjangoFilterBackend'
        filters.SearchFilter,
        filters.OrderingFilter,
    )


# ModelViewSet使用相应的HTTP谓词提供创建，读取，更新，删除（CRUD）操作所需的脚手架。
# 如果未在视图本身上设置，则REST_FRAMEWORK设置字典将控制身份验证，权限，分页和筛选的默认值。

# 继承DefaultsMixin类都将加入权限控制
# search_fields添加到所有ViewSet，实现字段搜索
# ordering_fields添加到所有ViewSet, 实现排序

# Sprint endpoint
class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints."""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
    filter_class = SprintFilter
    search_fields = ('name',)
    ordering_fields = ('end', 'name',)


# Task endpoint
class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    search_fields = ('name', 'description',)
    ordering_fields = ('name', 'order', 'started', 'due', 'completed',)


# User endpoint
class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD,)
