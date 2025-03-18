import requests
import yt_dlp
import os
YOUTUBE_API_KEY = "AIzaSyD_uhl8JT_N3qKC8Xi1VfPBYl8wOMEei3M"
DOWNLOAD_FOLDER = "media/songs/"

def search_youtube(query):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        return [
            {
                "title": item["snippet"]["title"],
                "video_id": item["id"]["videoId"],
                "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                "channel": item["snippet"]["channelTitle"],
                "youtube_url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            for item in data["items"]
        ]
    return []
def download_mp3(youtube_url):
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    ydl_opts = {
        "format": "bestaudio/best",
        "extractaudio": True,
        "audioformat": "mp3",
        "outtmpl": f"{DOWNLOAD_FOLDER}%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        return f"{DOWNLOAD_FOLDER}{info['title']}.mp3"