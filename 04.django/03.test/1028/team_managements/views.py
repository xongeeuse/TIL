from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Player, Game
from .serializers import (
    TeamListSerializer, TeamDetailSerializer, TeamCreateUpdateSerializer,
    PlayerListSerializer, PlayerDetailSerializer, PlayerCreateSerializer,
    PlayerUpdateSerializer, PlayerGameListSerializer, GameListSerializer, 
    GameDetailSerializer, GameCreateSerializer, GameUpdateSerializer,
)

# Team Views
@api_view(['GET', 'POST'])
def team_list_create(request):
    if request.method == 'GET':
        teams = get_list_or_404(Team)
        serializer = TeamListSerializer(teams, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TeamCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def team_detail_update_delete(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    
    if request.method == 'GET':
        serializer = TeamDetailSerializer(team)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TeamCreateUpdateSerializer(team, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def team_player_list_add(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.method == 'GET':
        players = team.players.all()
        serializer = PlayerListSerializer(players, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlayerCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(team=team)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        pass


@api_view(['GET'])
def team_games_home(request, team_id, notaway):
    # games = Game.objects.filter(home_team=team_id)
    games = get_list_or_404(Game, home_team=team_id)
    serializer = GameListSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def team_games_away(request, team_id):
    games = get_list_or_404(Game, away_team=team_id)
    serializer = GameListSerializer(games, many=True)
    return Response(serializer.data)


# Player Views
@api_view(['GET'])
def player_list(request):
    players = get_list_or_404(Player)
    serializer = PlayerListSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def player_detail_update_delete(request, player_id):
    player = get_object_or_404(Player, pk=player_id)

    if request.method == 'GET':
        serializer = PlayerDetailSerializer(player)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PlayerUpdateSerializer(player, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def player_games(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    games = get_list_or_404(Game, participations=player_id)
    serializer = PlayerGameListSerializer(games, many=True)
    return Response(serializer.data)


# Game Views
@api_view(['GET', 'POST'])
def game_list_create(request):
    if request.method == 'GET':
        games = get_list_or_404(Game)
        serializer = GameListSerializer(games, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GameCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def game_detail_update_delete(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    
    if request.method == 'GET':
        serializer = GameDetailSerializer(game)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = GameUpdateSerializer(game, data=request.POST, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)