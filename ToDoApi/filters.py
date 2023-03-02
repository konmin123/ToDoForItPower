from django.db.models.query import QuerySet
from django_filters import rest_framework as filters

from ToDoModels.models import Task


class TasksControlFilter(filters.FilterSet):

    class Meta:
        model = Task
        fields = ['executor', 'status', 'important']


class TasksImplementFilter(filters.FilterSet):

    class Meta:
        model = Task
        fields = ['author', 'important', 'status']


def parent_task_id_filter(queryset: QuerySet, parent_task_id):
    return queryset.filter(parent_task=parent_task_id)


def author_id_filter(queryset: QuerySet, author_id):
    return queryset.filter(author=author_id)


def executor_id_filter(queryset: QuerySet, executor_id):
    return queryset.filter(executor=executor_id)


def category_id_filter(queryset: QuerySet, category_id):
    return queryset.filter(category=category_id)


def important_filter(queryset):
    return queryset.filter(important=True)


def tasks_created_filter(queryset):
    return queryset.filter(status=1)


def tasks_process_filter(queryset):
    return queryset.filter(status=2)


def tasks_postponed_filter(queryset):
    return queryset.filter(status=3)


def completed_task_filter(queryset):
    return queryset.filter(status=4)
