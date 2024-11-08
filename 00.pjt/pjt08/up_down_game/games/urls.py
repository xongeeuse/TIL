from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('start/', views.start_game, name='start_game'),
    path('make-guess/<int:game_session_id>/', views.make_guess, name='make_guess'),
]