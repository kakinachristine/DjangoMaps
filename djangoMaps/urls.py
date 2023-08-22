from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Root URL pattern
    path('store_geolocation/', views.store_geolocation, name='store_geolocation'),
]
