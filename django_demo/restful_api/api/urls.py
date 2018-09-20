from rest_framework.routers import DefaultRouter

from . import views

# ViewSet routing extension
router = DefaultRouter()
# 指定一个URL前缀来注册路由
router.register(r'sprints', views.SprintViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
