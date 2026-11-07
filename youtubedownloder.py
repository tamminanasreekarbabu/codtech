
import yt_dlp

url = input("Enter YouTube video URL: ")

options = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(options) as downloader:
    downloader.download([url])

print("Download completed!")
