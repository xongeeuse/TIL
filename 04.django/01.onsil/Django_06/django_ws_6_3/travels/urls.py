from django.urls import path
from . import views

app_name = 'travels'
urlpatterns = [
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('update/<int:pk>/', views.update, name="update"),
    path('', views.index, name="index"),
]