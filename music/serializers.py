#music/serializer.py
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    youtube_embed_url = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = '__all__'  # Thêm mp3_url
    def get_youtube_embed_url(self, obj):
        return f"https://www.youtube.com/embed/{obj.youtube_url.split('=')[-1]}" if obj.youtube_url else None
    # def get_youtube_embed_url(self, obj):
    #     if "watch?v=" in obj.youtube_url:
    #         return obj.youtube_url.replace("watch?v=", "embed/")
    #     return obj.youtube_url
    


#export YOUTUBE_API_KEY = "AIzaSyD_uhl8JT_N3qKC8Xi1VfPBYl8wOMEei3M"