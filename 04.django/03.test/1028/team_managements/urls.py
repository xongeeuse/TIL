from django.urls import path
from . import views

urlpatterns = [
    # Team URLs
    path('teams/', views.team_list_create),
    path('teams/<int:team_id>/', views.team_detail_update_delete),
    path('teams/<int:team_id>/players/', views.team_player_list_add),

    path('teams/<int:team_id>/games/away/', views.team_games_away),
    path('teams/<int:team_id>/games/<str:notaway>/', views.team_games_home),

    # Player URLs
    path('players/', views.player_list),
    path('players/<int:player_id>/', views.player_detail_update_delete),
    
    path('players/<int:player_id>/games/', views.player_games),

    # Game URLs
    path('games/', views.game_list_create),
    path('games/<int:game_id>/', views.game_detail_update_delete),
]
