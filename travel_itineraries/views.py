from django.shortcuts import render
from .models import TravelItinerary

def travel_itinerary_list(request):
    travel_itineraries = TravelItinerary.objects.all()
    return render(request, 'travel_itineraries/travel_itinerary_list.html', {'travel_itineraries': travel_itineraries})

def hawaii(request):
    return render(request, 'hawaii.html')

def california(request):
    return render(request, 'california.html')

