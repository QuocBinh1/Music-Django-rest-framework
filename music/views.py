import requests
from rest_framework import viewsets
from .models import Song
from .serializers import SongSerializer

from rest_framework import generics


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

# @api_view(['GET'])
# def search_youtube(request):
#     # Lấy từ khóa (query) từ tham số GET, ví dụ: /api/search?q=lofi
#     query = request.GET.get('q', '')

#     # API Key của YouTube (bạn có thể lưu trong settings hoặc env)
#     API_KEY = settings.YOUTUBE_API_KEY
#     url = 'https://www.googleapis.com/youtube/v3/search'
#     params = {
#         'part': 'snippet',
#         'q': query,
#         'type': 'video',
#         'key': API_KEY,
#         'maxResults': 5  # Lấy 5 kết quả
#     }
    

#     response = requests.get(url, params=params)
#     data = response.json()

#     # Có thể kiểm tra data trước khi trả về
#     # data['items'] chứa danh sách video
#     return Response(data)

class SongListView(generics.ListAPIView):
    queryset = Song.object.all()
    serializer_class = SongSerializer

