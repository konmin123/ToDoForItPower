from django.urls import path

from . import views

urlpatterns = [
    path("api/new_task/", views.UserTaskCreateAPIView.as_view()),

    path("api/change_task/<int:pk>/",
         views.UserTaskUpdateDestroyAPIView.as_view()),

    path("api/change_status_task/<int:pk>/",
         views.ChangeImplementTaskStatusAPIView.as_view()),

    path("api/control_tasks/", views.UserControlTasksListAPIView.as_view()),

    path("api/implement_tasks/",
         views.UserImplementTasksListAPIView.as_view()),

    path("api/new_category/", views.CategoryCreateAPIView.as_view()),

    path("api/change_category/<int:pk>/",
         views.CatRetrieveUpdateDestroyAPIView.as_view()),
]
