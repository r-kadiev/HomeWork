# TODO настройте здесь urls для заданий get_car и search_car)
# Задание выполнено

from django.urls import path
from .views import get_car, search
urlpatterns = [
    path('<slug:pk>/', get_car),
    path('', search),
]
