from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def store_geolocation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        print(latitude)
        print(longitude)

        # Do something with the latitude and longitude data, like storing it in your database

        return HttpResponse("Geolocation data received and processed.")

def index(request):
    return render(request, 'geolocation.html')


