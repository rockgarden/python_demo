# 2 - 创建filter层
import django_filters
from django.contrib.auth import get_user_model

from .models import Sprint, Task

User = get_user_model()

# 处理值为Null的数据
class NullFilter(django_filters.BooleanFilter):
    """Filter on a field set as null or not."""

    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%s__isnull' % self.name: value})
        return qs


class SprintFilter(django_filters.FilterSet):
    end_min = django_filters.DateFilter(name='end', lookup_type='gte')
    end_max = django_filters.DateFilter(name='end', lookup_type='lte')

    class Meta:
        model = Sprint
        fields = ('end_min', 'end_max',)


class TaskFilter(django_filters.FilterSet):
    backlog = NullFilter(name='sprint')

    class Meta:
        model = Task
        fields = ('sprint', 'status', 'assigned', 'backlog',)

    # 更新 assigned 字段：使用User.USERNAME_FIELD作为字段引用而不是默认的pk。
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['assigned'].extra.update(
            {'to_field_name': User.USERNAME_FIELD})

# 另有ChoiceFilter,CharFilter等方式根据需要使用
