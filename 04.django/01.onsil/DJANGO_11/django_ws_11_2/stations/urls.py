from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.location_create),
    path('stations/', views.station_list),
    path('locations/<int:location_pk>/', views.station_create),
    path('stations/<int:station_pk>/', views.station_detail),
]
