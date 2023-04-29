from . import views
from django.urls import path

# TODO здесь необходимо настроить urls
# Задание выполнено
urlpatterns = [
    path("<int:id>/", views.CarView.as_view(), name="car"),
]
