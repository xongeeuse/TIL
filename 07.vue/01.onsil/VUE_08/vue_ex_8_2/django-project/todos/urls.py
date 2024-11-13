from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<int:todo_id>/', views.fetch_todo),
]
