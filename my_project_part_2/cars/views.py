from .models import Car
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404


# TODO ниже представлена функция, которую необходимо переписать на CBV 'CarView'
# Задание выполнено
class CarView(View):
    def get(self, request, id):
        car = get_object_or_404(Car, id=id)

        return JsonResponse({
                "id": car.id,
                "slug": car.slug,
                "name": car.name,
                "brand": car.brand,
                "address": car.address,
                "description": car.description,
                "status": car.status,
                "created": car.created,
            }, safe=False)
