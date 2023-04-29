from . import views
from django.urls import path

# TODO здесь необходимо настроить urls
urlpatterns = [
   path("feedback/", views.FeedbackView.as_view(), name="feedback"),
   path("feedback/<int:pk>/", views.FeedbackEntityView.as_view(), name="feedback_entity"),
   path("destinations/", views.DestinationView.as_view(), name="destinations"),
   path("destinations/<int:id>/", views.DestinationEntityView.as_view(), name="destination_entity"),
   path("gen-destination/", views.DestinationListView.as_view(), name="destinations_list"),
   path("gen-destination/<int:pk>/", views.DestinationDetailView.as_view(), name="destination_detail")
]
