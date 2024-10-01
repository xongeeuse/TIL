
from django.urls import path
from . import views

app_name = 'buckets'
urlpatterns = [
    path('', views.index, name='index',),
    path('about/', views.about, name='about',),
    path('<int:bucket_pk>/', views.detail, name='detail',),
    path('create/', views.create, name='create'),
    path('<int:bucket_pk>/update/', views.update, name='update'),
    path('<int:bucket_pk>/delete/', views.delete, name='delete'),
]

