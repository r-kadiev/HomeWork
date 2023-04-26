from django.http import JsonResponse
from .models import Car


def get_car(request, pk):
    # TODO напишите view-функцию здесь (Readme.md, Задание get_car)
    # Задание выполнено

    if request.method == "GET":
        cars = Car.objects.all().filter(id=pk)
        response = []
        for car in cars:

            response.append(
                {'slug': car.slug,
                    'name': car.name,
                    'brand': car.brand,
                    'address': car.address,
                    'description': car.description,
                    'status': car.status,
                    'created': car.created,
                }
            )
        return JsonResponse(response, safe=False)


def search(request):
    # TODO напишите view-функцию здесь (Readme.md, Задание car_search)
    # Задание выполнено

    if request.method == "GET":
        cars = Car.objects.all()
        search_text = request.GET.get("search")

        if search_text:
            cars = cars.filter(brand=search_text)
            response = []

            for car in cars:
                response.append(
                    {"id": car.id,
                        "name": car.name,
                        "brand": car.brand,
                        "status": car.status,
                    }
                )

            return JsonResponse(response, safe=False)
