# spending/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="spending_index"),
]
