from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="tasks_index"),
    path("create/", views.create_task, name="create_task"),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
]
