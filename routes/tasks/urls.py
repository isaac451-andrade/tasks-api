from django.urls import path
from .views import *

urlpatterns = [
    path("", TaskListView.as_view(), name="list_tasks_from_user"),
    path("create/", task_create_view, name="create_tasks_for_user"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="delete_task_from_user"),
    path("update/<int:pk>/", task_update_view, name="update_task_from_user"),

]