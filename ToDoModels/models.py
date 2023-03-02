from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


def _get_datetime():
    return timezone.now() + timedelta(hours=72)


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Task(models.Model):
    class Status(models.IntegerChoices):
        CREATED = 1, _('Создана')
        PROCESS = 2, _('В работе')
        POSTPONED = 3, _('Отложена')
        COMPLETED = 4, _('Выполнена')

    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    text = models.TextField(default='', verbose_name='Текст')
    parent_task = models.ForeignKey(
        'Task', default=None, on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ForeignKey(
        Category, default=None, on_delete=models.SET_NULL, blank=True,
        null=True
    )
    status = models.IntegerField(
        default=Status.CREATED, choices=Status.choices, verbose_name='Статус'
    )
    important = models.BooleanField(default=False, verbose_name='Важная')
    create_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания'
    )
    update_at = models.DateTimeField(
        auto_now=True, verbose_name='Время изменения'
    )
    execution_time = models.DateTimeField(
        default=_get_datetime, verbose_name='Срок выполнения'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks'
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='ex_tasks'
    )

    def __str__(self):
        return f"Запись №{self.id}"




