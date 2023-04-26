# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
# Задание выполнено
from django.urls import path

from .views import courses, new_courses, get_course, search

urlpatterns = [
    path("", courses),
    path("search/", search),
    path("new_courses/", new_courses),
    path("<slug:slug>/", get_course),
]
