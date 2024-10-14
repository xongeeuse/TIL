from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('mypage/', views.my_page, name='my_page'),
    path('<int:todo_pk>/', views.detail, name='detail'),
    path('<int:todo_pk>/delete/', views.delete, name='delete'),
    path('<int:todo_pk>/update/', views.update, name='update'),
    path('<int:todo_pk>/recommend/', views.recommend, name='recommend'),
]