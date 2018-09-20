# Create your models here.
from django.conf import settings
from django.db import models
# from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


# @python_2_unicode_compatible
class Sprint(models.Model):
    """Development iteration period."""

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end


class Task(models.Model):
    """Unit of work to be done for the sprint."""

    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Not Started')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题
    # CASCADE：此值设置，是级联删除。
    # PROTECT：此值设置，是会报完整性错误。
    # SET_NULL：此值设置，会把外键设置为null，前提是允许为null。
    # SET_DEFAULT：此值设置，会把设置为外键的默认值。
    # SET()：此值设置，会调用外面的值，可以是一个函数。
    sprint = models.ForeignKey(Sprint, blank=True, null=True, on_delete=models.CASCADE)

    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)

    # 引入settings.AUTH_USER_MODEL支持默认用户模型
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.CASCADE)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
