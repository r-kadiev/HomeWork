from .models import Course
from django.http import JsonResponse


def courses(request):

    if request.method == "GET":

        courses_list = Course.objects.all()
        response = []
        for course in courses_list:
            response.append(
                {
                    "id": course.id,
                    "slug": course.slug,
                    "author": course.author,
                    "description": course.description,
                    "start_day": course.start_day,
                    "status": course.status,
                    "created": course.created,
                }
            )
        return JsonResponse(response, safe=False)


def new_courses(request):
    # TODO напишите здесь view-функцию (задание new_courses)
    # Задание выполнено

    if request.method == "GET":
        new_courses_list = Course.objects.all()
        response = []
        for new_course_list in new_courses_list:
            if new_course_list.status == "new":
                response.append(
                    {
                        "id": new_course_list.id,
                        "slug": new_course_list.slug,
                        "author": new_course_list.author,
                        "description": new_course_list.description,
                        "start_day": new_course_list.start_day,
                        "status": new_course_list.status,
                        "created": new_course_list.created,
                    }
                )

        return JsonResponse(response, safe=False)


def get_course(request, slug):

    # TODO напишите здесь view-функцию (задание find_by_name)
    # Задание выполнено

    if request.method == "GET":
        response = []
        courses_list = Course.objects.all().filter(slug=slug)

        for course_list in courses_list:
            response.append({
                "id": course_list.id,
                "slug": course_list.slug,
                "author": course_list.author,
                "description": course_list.description,
                "start_day": course_list.start_day,
                "status": course_list.status,
                "created": course_list.created,

            })
        return JsonResponse(response, safe=False)


def search(request):
    # TODO напишите здесь view-функцию (задание who's author)
    # Задание выполнено

    if request.method == "GET":
        courses_list = Course.objects.all()
        search_text = request.GET.get("author", None)

        if search_text:
            courses_list = courses_list.filter(author=search_text)
            response = []
            for course in courses_list:
                response.append(
                    {
                        "id": course.id,
                        "slug": course.slug,
                        "author": course.author,
                        "description": course.description,
                        "start_day": course.start_day,
                        "status": course.status,
                        "created": course.created,
                    }
                )
            return JsonResponse(response, safe=False)
