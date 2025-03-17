from django.db import models

# Create your models here.
class Song(models.Model):
    youtube_url = models.URLField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    artist = models.CharField(max_length=255, blank=True)
    thumbnail = models.URLField(blank=True)
    mp3_url = models.URLField(blank=True)  

    def __str__(self):
        return self.title
    