from rest_framework import serializers
from .models import Post, Category, Comment

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'category')