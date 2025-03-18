#music/views.py
import requests
from rest_framework.response  import Response
from .models import Song
from .serializers import SongSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .utils import search_youtube, download_mp3


@api_view(['POST'])
def save_song(request):
    data = request.data
    video_id = data.get('video_id', '')

    # Kiểm tra nếu video_id không hợp lệ
    if not video_id:
        return Response({"error": "video_id is required"}, status=400)

    song, created = Song.objects.update_or_create(
        video_id=video_id,  # ✅ Dùng video_id để kiểm tra trùng lặp
        defaults={  # Cập nhật thông tin nếu bài hát đã có
            "title": data.get('title', ''),
            "artist": data.get('artist', ''),
            "youtube_url": data.get('youtube_url', ''),
            "thumbnail": data.get('thumbnail', ''),
        }
    )

    return Response(SongSerializer(song).data)
class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SearchSongView(APIView):
    def get(self, request):
        query = request.GET.get("q")
        if not query:
            return Response({"error": "Query parameter is required"}, status=400)
        
        results = search_youtube(query)
        return Response(results)

class DownloadSongView(APIView):
    def post(self, request):
        youtube_url = request.data.get("youtube_url", "")
        title = request.data.get("title", "")
        artist = request.data.get("artist", "")
        thumbnail = request.data.get("thumbnail", "")

        if not youtube_url:
            return Response({"error": "youtube_url is required"}, status=400)

        mp3_path = download_mp3(youtube_url)

        # Kiểm tra nếu bài hát đã tồn tại
        song, created = Song.objects.get_or_create(
            youtube_url=youtube_url,
            defaults={
                "title": title,
                "artist": artist,
                "thumbnail": thumbnail,
                "mp3_url": "",  # Chưa tải mp3, để trống
            }
        )
        if created or not song.mp3_url:  # Nếu bài hát mới hoặc chưa có mp3_url
            mp3_path = download_mp3(youtube_url)
            song.mp3_url = mp3_path
            song.save()
        return Response(SongSerializer(song).data)
