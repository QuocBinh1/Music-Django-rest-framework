#music/models.py
from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255, unique=True, null=True, blank=True) 
    youtube_url = models.URLField()
    youtube_embed_url = models.URLField(null=True, blank=True) 
    thumbnail = models.URLField()
    mp3_url = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.title
    