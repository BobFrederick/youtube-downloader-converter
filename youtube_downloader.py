import os
import pytube

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)


def download_playlist_audio(url):
    playlist = pytube.Playlist(url)
    # get playlist title
    playlist_title = playlist.title
    print(f"Downloading playlist: {playlist_title}")
    # remove special characters from the title
    playlist_title = "".join(x for x in playlist_title if x.isalnum() or x in [" ", "-", "_"]).rstrip()
    # create a folder with the playlist title in the /downloads folder
    if os.path.exists(f"downloads/{playlist_title}") is False:
        os.makedirs(f"downloads/{playlist_title}", exist_ok=True)
    for i, video in enumerate(playlist.videos):
        print(f"----Downloading {video.title} - {video.author} ({i + 1}/{len(playlist.video_urls)})...")
        try:
            audio_file_stream = video.streams.get_audio_only()
            if audio_file_stream is None:
                continue
            audio_file_stream.download(f"downloads/{playlist_title}")
        except:
            print(f"Error downloading {video.title} - {video.author} ({i + 1}/{len(playlist.video_urls)})")
            continue
    print(f"Download of {playlist_title} finished!")


def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links