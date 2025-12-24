
from django.conf import settings
from django.db import models
from django.db import models 
from django.contrib.auth.models import User

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
    media_type = models.CharField(max_length=10, choices=[("book", "Book"), ("movie", "Movie")])
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    # Sample 1
    sample_title_1 = models.CharField(max_length=200, blank=True, null=True)
    sample_author_director_1 = models.CharField(max_length=200, blank=True, null=True)
    sample_description_1 = models.TextField(blank=True, null=True)
    sample_image_1 = models.ImageField(upload_to="club_samples/", blank=True, null=True)
    sample_link_1 = models.URLField(blank=True, null=True)

    # Sample 2
    sample_title_2 = models.CharField(max_length=200, blank=True, null=True)
    sample_author_director_2 = models.CharField(max_length=200, blank=True, null=True)
    sample_description_2 = models.TextField(blank=True, null=True)
    sample_image_2 = models.ImageField(upload_to="club_samples/", blank=True, null=True)
    sample_link_2 = models.URLField(blank=True, null=True)

    members = models.ManyToManyField(User, related_name="clubs", blank=True)

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
    club = models.ForeignKey("Club", on_delete=models.CASCADE, related_name="feedbacks")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.club.name}"



