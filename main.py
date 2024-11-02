import yt_dlp

url = input("Enter video URL: ")

ydl_opts = {
    'format': "best[height<=1080]"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])