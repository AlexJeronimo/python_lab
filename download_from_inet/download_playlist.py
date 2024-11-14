from pytube import Playlist
from pytube import YouTube
from pytube.cli import on_progress

link = input("Enter Youtube playlist link: \n")

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    stream = video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    stream.download(f"E:\\Downloads\\{yt_playlist.title.translate({ord(i): None for i in ':?*'})}\\")
    print("Video downloaded: ", video.title)

print(f"\nAll videos from {yt_playlist.title} are downloaded")

# https://www.youtube.com/playlist?list=PLGQiJX6wM-zzcPye1y7gpyJO0uH7NMNP7