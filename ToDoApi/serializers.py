from rest_framework import serializers

from ToDoModels.models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.CurrentUserDefault()

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("author",)


class ChangeStatusTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("status",)


class QueryParamsFilterSerializer(serializers.Serializer):
    status = serializers.ListField(
        child=serializers.ChoiceField(choices=Task.Status.choices),
        required=False
    )
