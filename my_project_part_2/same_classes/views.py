import http.client

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Feedback, Destination
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
import json


@method_decorator(csrf_exempt, name='dispatch')
class FeedbackView(View):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        response = []
        for feedback in feedbacks:
            response.append({
                "correlation_id": feedback.correlation_id,
                "user_feedback": feedback.user_feedback,
                "user_feedback_timestamp": feedback.user_feedback_timestamp,
                "closed": feedback.closed
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        feedback_data = json.loads(request.body)

        feedback = Feedback()
        feedback.user_feedback = feedback_data["user_feedback"]
        feedback.closed = feedback_data.get("closed", False)

        try:
            feedback.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        feedback.save()
        return JsonResponse({
            "id": feedback.id,
            "correlation_id": feedback.correlation_id,
        })


class FeedbackEntityView(View):
    def get(self, request, id):
        feedback = get_object_or_404(Feedback, id=id)

        return JsonResponse({
            "id": feedback.id,
            "correlation_id": feedback.correlation_id,
            "user_feedback": feedback.user_feedback,
            "user_feedback_timestamp": feedback.user_feedback_timestamp,
            "closed": feedback.closed
        })

# TODO ниже следует реализовать CBV для модели Destination
@method_decorator(csrf_exempt, name='dispatch')
class DestinationView(View):
    def get(self, request):
        destinations = Destination.objects.all()
        response = []
        for destination in destinations:
            response.append({
                'id': destination.id,
                'name': destination.name,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        destination_data = json.loads(request.body)

        destination = Destination()
        destination.id = destination_data["id"]
        destination.name = destination_data["name"]
        destination.to_name = destination_data["to_name"]
        destination.flag = destination_data["flag"]
        destination.visa_id = destination_data["visa_id"]
        destination.covid_status = destination_data["covid_status"]

        try:
            destination.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        destination.save()
        return JsonResponse({
            "id": destination.id,
            "name": destination.name
        })




class DestinationEntityView(View):
    def get(self, request, id):
        destination = get_object_or_404(Destination, id=id)

        return JsonResponse({
            'id': destination.id,
            'name': destination.name,
            'visa_id': destination.visa_id,
            'covid_status': destination.covid_status,
        })


# TODO ниже следует реализовать generics(ListView, DetailView) CBV для модели Destination
class DestinationListView(ListView):

    def get(self, request):
        destinations = Destination.objects.all()
        response = []
        for destination in destinations:
            response.append({
                'id': destination.id,
                'name': destination.name,
            })
        return JsonResponse(response, safe=False)



    model = Destination


class DestinationDetailView(DetailView):

    model = Destination

    def get(self, request, *args, **kwargs):
        destination = self.get_object()
        return JsonResponse({
            "id": destination.id,
            "name": destination.name,
        })

