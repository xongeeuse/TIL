from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 조회(타입: 쿼리셋, but 쿼리셋은 장고에서 사용하는 데이터 타입)
        articles = Article.objects.all()
        # 변환하기 쉬운 포맷으로 전환(직렬화==Serialize)
        # 다중데이터라 many=True 옵션 설정
        serializer = ArticleListSerializer(articles, many=True)
        # Serialized data 객체에서 실제 데이터를 추출
        return Response(serializer.data)
    elif request.method == 'POST':
        # 모델시리얼라이저를 사용해서 사용자 입력 데이터를 받아 직렬화를 진행
        serializer = ArticleListSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 저장 성공 후 201 응답 상태코드를 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사 실패 후 400 응답 상태코드를 반환
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)