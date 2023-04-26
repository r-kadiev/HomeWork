from django.urls import path
from .views import statistics

# здесь url уже настроен, ничего менять не нужно
urlpatterns = [
    path("statistics/", statistics),
]
