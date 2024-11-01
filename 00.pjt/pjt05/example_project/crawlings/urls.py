from django.urls import path
from . import views

app_name="crawlings"
urlpatterns = [
    path('', views.index, name="index"),
]
