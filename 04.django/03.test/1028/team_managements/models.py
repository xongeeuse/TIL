from django.db import models

# 모델 정보를 수정하는 문항이 없습니다.
# 모델 정보는 수정이 불가하며 수정시 loaddata 에 문제가 발생할 수 있습니다.
# 모델 정보 수정시 0점 처리됩니다.

# 팀 정보를 저장하는 모델 (수정 불가)
class Team(models.Model):
    # 팀 이름
    name = models.CharField(max_length=255)
    # 팀의 연고지 도시
    city = models.CharField(max_length=255)
    # 팀 감독 이름
    coach_name = models.CharField(max_length=255)
    # 팀 설립 연도
    founded = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.city}"  # 팀 이름과 연고지를 문자열로 반환


# 선수 정보를 저장하는 모델 (수정 불가)
class Player(models.Model):
    # Team 모델과 연결된 Foreign Key - 한 팀에 여러 선수가 포함될 수 있음
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    # 선수 이름
    name = models.CharField(max_length=255)
    # 선수 포지션 (예: 골키퍼, 수비수 등)
    position = models.CharField(max_length=50)
    # 선수 등번호
    number = models.PositiveIntegerField()
    # 선수 생년월일
    birthdate = models.DateField()
    # 선수 활동 여부 (True: 활동 중, False: 은퇴 또는 비활동)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - #{self.number}"  # 선수 이름과 등번호를 문자열로 반환


# 경기 정보를 저장하는 모델 (수정 불가)
class Game(models.Model):
    # Team 모델과 연결된 Foreign Key - 홈팀과 원정팀 (Many-to-One 관계)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
    # 경기 날짜
    date = models.DateField()
    # 경기 장소
    location = models.CharField(max_length=255)
    # 홈팀 점수
    home_team_score = models.PositiveIntegerField(default=0)
    # 원정팀 점수
    away_team_score = models.PositiveIntegerField(default=0)
    # 참가한 선수 정보
    participations = models.ManyToManyField(Player, related_name='participations')

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} on {self.date}"  # 경기 정보 문자열로 반환

