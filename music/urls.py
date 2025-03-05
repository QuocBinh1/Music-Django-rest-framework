from django.urls import path
from .views import search_youtube

urlpatterns = [
    path('search/', search_youtube, name='search-youtube'),
]
from django.urls import path
from .views import search_youtube

urlpatterns = [
    path('search/', search_youtube, name='search-youtube'),
]
