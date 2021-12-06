from django.db import models

from users.models import User

class Movie(models.Model):
    title   = models.CharField(max_length=80)
    year    = models.CharField(max_length=45)
    rating  = models.DecimalField(null=True, max_digits=2, decimal_places=1)
    genres  = models.TextField()
    summary = models.TextField()

    class Meta:
        db_table = 'movies'

class MovieReview(models.Model): 
    movie      = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    text       = models.TextField()
    rating     = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        db_table = 'movie_reviews'

class MovieReviewVote(models.Model): 
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie_review_vote'