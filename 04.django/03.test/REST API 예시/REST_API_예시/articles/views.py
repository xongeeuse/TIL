from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Article
from .serializers import (
    ArticleSerializer,
    ArticleListSerializer
)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        message = {
            '삭제된 파일의 정보': {
                'msg':f'{article.pk}번 파일 {article.title} 삭제'
                },
            '응답 코드' : 204}
        article.delete()
        return Response(message, status=status.HTTP_204_NO_CONTENT)