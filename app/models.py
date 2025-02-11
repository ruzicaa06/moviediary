from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    length = models.IntegerField()
    review = models.TextField()
    rating = models.FloatField()
    date_watched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

