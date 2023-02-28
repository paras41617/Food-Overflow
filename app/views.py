from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import FoodProvider

def provider_list(request):
    user_location = request.user.location  # assuming user location is stored in user object
    providers = FoodProvider.objects.annotate(distance=Distance('location', Point(user_location))).order_by('distance')
    return render(request, 'provider_list.html', {'providers': providers})