from django.urls import path
from .views import travel_itinerary_list, hawaii, california

urlpatterns = [
    path('', travel_itinerary_list, name='travel_itinerary_list'),
    path('hawaii/', hawaii, name='hawaii'),
    path('california/', california, name='california'),
]
