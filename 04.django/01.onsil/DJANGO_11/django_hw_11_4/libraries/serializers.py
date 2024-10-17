from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):
    class BookReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('content', 'score',)

    number_of_reviews = serializers.IntegerField(source='review_set.count', read_only=True)
    review_set = BookReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class BookIsbnSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('isbn',)
    book = BookIsbnSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)