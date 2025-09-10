from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="spending_index"),
    path("create/", views.create_expense, name="create_expense"),
    path("update/<int:pk>/", views.update_expense, name="update_expense"),
    path("delete/<int:pk>/", views.delete_expense, name="delete_expense"),
]
