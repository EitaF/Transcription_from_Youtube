from yt_dlp import YoutubeDL
import os

def download_video(url, output_folderpath):
    ydl_video_opts = {
        "outtmpl" : os.path.join(output_folderpath, "%(id)s" + "_.mp3",)
        "format" : "bestaudio
    }

    with YoutubeDL(ydl_video_opts) as ydl:
        result = ydl.download([url])
