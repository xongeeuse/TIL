from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<int:todo_pk>/', views.todo_detail),
    path('todos/<int:todo_pk>/recommends/', views.recommend_create),
]
