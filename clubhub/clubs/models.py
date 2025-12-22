
from django.conf import settings
from django.db import models

class Genre(models.Model):
    MEDIA_CHOICES = [
        ('book', 'Book'),
        ('movie', 'Movie'),
    ]
    name = models.CharField(max_length=50)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_media_type_display()})"


class Club(models.Model):
    name = models.CharField(max_length=100)
    media_type = models.CharField(max_length=10, choices=Genre.MEDIA_CHOICES)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'club')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
