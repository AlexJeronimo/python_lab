from pytube import Playlist

link = input("Enter Youtube playlist link: \n")

yt_playlist = Playlist(link)

print(f'Playlist "{yt_playlist.title}" links:')
for link in yt_playlist.video_urls:
    print(f"{link}")

