from rest_framework import serializers

from .models import Movie, MovieReview

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields ='__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    reviews = MovieReviewSerializer(many=True)

    class Meta:
        model  = Movie
        fields = ('id', 'title', 'year', 'rating', 'genres', 'summary', 'reviews')

