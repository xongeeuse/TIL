from django.urls import path
from . import views


app_name = 'diaries'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:diary_pk>/comments/', views.comments_create, name='comments_create'),
    path('comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:diary_pk>/likes/', views.likes, name='likes'),
]