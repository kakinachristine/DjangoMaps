from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient

import json


@csrf_exempt
def store_geolocation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        print(latitude)
        print(longitude)

        # Connect to MongoDB and store the geolocation data
        connection_string = "mongodb+srv://your-connection-string"
        client = MongoClient(connection_string)
        db = client["your-database-name"]
        collection = db["your-collection-name"]

        # Store the geolocation data in the collection
        collection.insert_one({"latitude": latitude, "longitude": longitude})

        return HttpResponse("Geolocation data received and processed.")


def index(request):
    return render(request, 'mongo_template.html')


def mongo_view(request):
    # Replace with your MongoDB Atlas connection string
    connection_string = "mongodb+srv://V:V@Cluster0-name.mongodb.net/test"

    client = MongoClient(connection_string)
    db = client["V"]

    # Create a new collection named "geolocation_data"
    collection_name = "geolocation_data"
    db.create_collection(collection_name)

    # Check if the collection exists
    if collection_name in db.list_collection_names():
        collection_exists = True
    else:
        # Create a new collection
        db.create_collection(collection_name)
        collection_exists = False

    # Render a template and pass the collection existence status to it
    return render(request, 'mongo_template.html', {'collection_exists': collection_exists})
