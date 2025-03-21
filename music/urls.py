#music/urls.py
from django.urls import path
from .views import SongListView , DownloadSongView , SearchSongView,save_song , get_youtube_songs


urlpatterns = [
    path('songs/', SongListView.as_view(), name="song_list"),
    path('download/', DownloadSongView.as_view(), name='download-song'),
    path('search/', SearchSongView.as_view(), name='search-song'),
    path('save/', save_song, name='save-song'),
    path("youtube-songs/", get_youtube_songs , name = "youtube-songs" ),

]
