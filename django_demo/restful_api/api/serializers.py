from datetime import date

from django.contrib.auth import get_user_model
# ugettext_lazy to make the error messages translatable.
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
# 提供返回完全限定URL或视图名称的urlresolver函数
from rest_framework.reverse import reverse

from .models import Sprint, Task

User = get_user_model()


# 通过API对模型进行序列化和反序列化(serialized and deserialized)
# 每个序列化程序都有一个响应正文的新的只读链接字段links。
# 要填充链接links值，每个序列化程序都有一个get_links方法来构建相关链接。


class SprintSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end', 'links',)

    def get_links(self, obj):
        """
        get_links不使用Django的标准reverse，而是使用内置于django-rest-framework的修改过的版本。
        这将返回完整的URI，包括主机名和协议，以及路径。
        为此，reverse需要当前请求，当我们使用标准ViewSets时，默认情况下会将其传递到序列化程序上下文中。
        :param obj:
        :return:
        """
        request = self.context['request']
        return {
            'self': reverse('sprint-detail',
                            kwargs={'pk': obj.pk}, request=request),
            'tasks': reverse('task-list',
                             request=request) + '?sprint={}'.format(obj.pk),
        }

    def validate_end(self, value):
        new = self.instance is None
        changed = self.instance and self.instance.end != value
        if (new or changed) and (value < date.today()):
            msg = _('End date cannot be in the past.')
            raise serializers.ValidationError(msg)
        return value


class TaskSerializer(serializers.ModelSerializer):
    # 用SlugRelatedField来实现通过用户名来引用用户
    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False, allow_null=True,
        queryset=User.objects.all())

    # status_display是要序列化的只读字段，它返回序列化程序上get_status_display方法的值。
    status_display = serializers.SerializerMethodField()

    links = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'sprint', 'status',
                  'status_display', 'order', 'assigned', 'started', 'due',
                  'completed', 'links',)

    def get_status_display(self, obj):
        """
        显示状态文本
        :param obj:
        :return:
        """
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('task-detail',
                            kwargs={'pk': obj.pk}, request=request),
            'sprint': None,
            'assigned': None
        }

        # 分配给sprint的任务应该指向其sprint。
        # 如果已分配用户，您还可以通过反转URL从任务链接到其分配的用户。
        if obj.sprint_id:
            links['sprint'] = reverse('sprint-detail',
                                      kwargs={'pk': obj.sprint_id}, request=request)
        if obj.assigned:
            links['assigned'] = reverse('user-detail',
                                        kwargs={User.USERNAME_FIELD: obj.assigned}, request=request)
        return links

    def validate_sprint(self, value):
        if self.instance and self.instance.pk:
            if value != self.instance.sprint:
                if self.instance.status == Task.STATUS_DONE:
                    msg = _('Cannot change the sprint of a completed task.')
                    raise serializers.ValidationError(msg)
                if value and value.end < date.today():
                    msg = _('Cannot assign tasks to past sprints.')
                    raise serializers.ValidationError(msg)
        else:
            if value and value.end < date.today():
                msg = _('Cannot add tasks to past sprints.')
                raise serializers.ValidationError(msg)
        return value

    def validate(self, attrs):
        sprint = attrs.get('sprint')
        status = attrs.get('status', Task.STATUS_TODO)
        started = attrs.get('started')
        completed = attrs.get('completed')
        if not sprint and status != Task.STATUS_TODO:
            msg = _('Backlog tasks must have "Not Started" status.')
            raise serializers.ValidationError(msg)
        if started and status == Task.STATUS_TODO:
            msg = _('Started date cannot be set for not started tasks.')
            raise serializers.ValidationError(msg)
        if completed and status != Task.STATUS_DONE:
            msg = _('Completed date cannot be set for uncompleted tasks.')
            raise serializers.ValidationError(msg)
        return attrs


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)  # get_full_name是一个方法
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name',
                  'is_active', 'links')

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail',
                            kwargs={User.USERNAME_FIELD: username}, request=request),
            'tasks': '{}?assigned={}'.format(
                reverse('task-list', request=request), username)
        }
