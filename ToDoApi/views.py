from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ToDoModels.models import Task, Category
from ToDoApi import serializers, filters


class UserTaskCreateAPIView(generics.CreateAPIView):
    """"Создание новых задач. Только для авторизованных пользователей."""
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserTaskUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Изменение, удаление задач. Для авторизованных пользователей,
    только автор может удалять/редактировать задачу."""
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def filter_queryset(self, queryset):
        queryset = filters.author_id_filter(
            queryset,
            author_id=self.request.user.id,
        )
        return queryset


class ChangeImplementTaskStatusAPIView(generics.UpdateAPIView):
    """Авторизованный исполнитель меняет статус выполнения своей задачи."""
    queryset = Task.objects.all()
    serializer_class = serializers.ChangeStatusTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def filter_queryset(self, queryset):
        query_params = serializers.QueryParamsFilterSerializer(
            data=self.request.query_params
        )
        query_params.is_valid(raise_exception=True)
        queryset = filters.executor_id_filter(
            queryset, executor_id=self.request.user.id
        )
        return queryset


class UserControlTasksListAPIView(generics.ListAPIView):
    """Получение списка задач созданных авторизованным пользователем,
   Фильтры: исполнитель, важность, статус."""
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.TasksControlFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def filter_queryset(self, queryset):
        query_params = serializers.QueryParamsFilterSerializer(
            data=self.request.query_params
        )
        query_params.is_valid(raise_exception=True)
        queryset = filters.author_id_filter(
            queryset, author_id=self.request.user.id
        )
        executor_id = query_params.data.get("executor")
        if executor_id:
            queryset = queryset.filter(executor=executor_id)
        status = query_params.data.get("status")
        if status:
            queryset = queryset.filter(status__in=query_params.data["status"])
        important = self.request.query_params.get("important")
        if important:
            queryset = queryset.filter(important=important)
        return queryset


class UserImplementTasksListAPIView(generics.ListAPIView):
    """Получение списка задач исполнителем которых является авторизованный
    пользователь. Фильтры: автор, важность, статус."""
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.TasksImplementFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def filter_queryset(self, queryset):
        query_params = serializers.QueryParamsFilterSerializer(
            data=self.request.query_params
        )
        query_params.is_valid(raise_exception=True)
        queryset = filters.executor_id_filter(
            queryset, executor_id=self.request.user.id
        )
        author_id = self.request.query_params.get("author")
        if author_id:
            queryset = queryset.filter(author=author_id)
        status = query_params.data.get("status")
        if status:
            queryset = queryset.filter(status__in=query_params.data["status"])
        important = self.request.query_params.get("important")
        if important:
            queryset = queryset.filter(important=important)
        return queryset


class CategoryCreateAPIView(generics.CreateAPIView):
    """"Создание новых категорий. Только для авторизованных пользователей."""
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CatRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """"Изменение/удаление существующих категорий задач.
    Только для авторизованных пользователей."""
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
