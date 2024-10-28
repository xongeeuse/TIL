from rest_framework import serializers
from .models import Team, Player, Game


# Team 모델의 Read(list) 시리얼라이저
class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'city',)


# Team 모델의 Read(detail) 시리얼라이저
class TeamDetailSerializer(serializers.ModelSerializer):
    class PlayersOfTheTeamSerializer(serializers.ModelSerializer):
        class Meta:
            model = Player
            fields = '__all__'
    
    # players = PlayersOfTheTeamSerializer(many=True, read_only=True)
    player_count = serializers.IntegerField(source='players.count', read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


# Team 모델의 Create/Update 시리얼라이저
class TeamCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


# Player 모델의 Read(list) 시리얼라이저
class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


# Player 모델의 Read(detail) 시리얼라이저
class PlayerDetailSerializer(serializers.ModelSerializer):
    class TeamDetailofthePlayerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Team
            fields = '__all__'
    
    team = TeamDetailofthePlayerSerializer(serializers.ModelSerializer)
        
    class Meta:
        model = Player
        fields = '__all__'


# Player 모델의 Create/Update 시리얼라이저
class PlayerCreateSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Player
        fields = '__all__'


# Player 모델의 Create/Update 시리얼라이저
class PlayerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


# Player가 참여한 Game List 시리얼라이저
class PlayerGameListSerializer(serializers.ModelSerializer):
    home_team = serializers.StringRelatedField()
    away_team = serializers.StringRelatedField()

    class Meta:
        model = Game
        fields = ['home_team', 'away_team', 'date']


# Game 모델의 Read(List) 시리얼라이저
class GameListSerializer(serializers.ModelSerializer):
    home_team = serializers.StringRelatedField()
    away_team = serializers.StringRelatedField()

    class Meta:
        model = Game
        # fields = '__all__'
        exclude = ['participations']


# Game 모델의 Read(detail) 시리얼라이저
class GameDetailSerializer(serializers.ModelSerializer):
    home_team = TeamListSerializer(read_only=True)
    away_team = TeamListSerializer(read_only=True)
    participations = PlayerListSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'


# Game 모델의 Create/Update 시리얼라이저
class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


# Game 모델의 Create/Update 시리얼라이저
class GameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

