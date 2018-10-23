from rest_framework.routers import DefaultRouter

from . import views

# 更改trailing_slash选项处理url结尾的斜杠
router = DefaultRouter(trailing_slash=False)
router.register(r'sprints', views.SprintViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
