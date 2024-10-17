from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)
    # comment_set 역참조 데이터를 override
    # 쿼리셋 데이터를 조회하는 형태니까 many 옵션 잊지 마세요!
    # `models.py`에서 related_name 사용했다면 `comment_set` 자리에 그 이름 넣어줘야 함!
    number_of_comments = serializers.IntegerField(source='comment_set.count', read_only=True)
    comment_set = CommentDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # 기존 article 데이터 값을 override
    # but, 기존 필드를 override하게 되면 Meta클래스의 read_only_fields를 사용할 수 없음
    # 모델 시리얼라이저의 read_only 인자 값으로 재설정
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        # fields에 작성된 필드는 모두 유효성 검사 목록에 포함됨
        fields = '__all__'
        # 외래 키 필드를 읽기전용으로 설정
        # 이유는? 외래 키 데이터는
        # 1. 유효성 검사에서는 제외
        # 2. 결과 데이터에는 포함하고 싶음
        read_only_fields = ('article',)


# class CommentCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         exclude = ('article',)