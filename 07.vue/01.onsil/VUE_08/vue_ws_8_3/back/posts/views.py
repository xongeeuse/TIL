from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Post, Category, Comment
from .serializers import PostListSerializer


# Create your views here.
@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = get_list_or_404(Post)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
        
    pass