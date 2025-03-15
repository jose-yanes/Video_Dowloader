import yt_dlp
from dotenv import load_dotenv
import os

load_dotenv()

def downloader(urlObj):
    DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY")
    
    if urlObj["format"] == "video":
        ydl_opts = {
                "paths": {"home": f"{DOWNLOAD_DIRECTORY}videos"},
                "writethumbnail": True,
                "embed-thumbnail": True,
                "outtmpl": "%(channel)s/%(title)s.%(ext)s",
                "postprocessors": [
                    {
                        "key": "FFmpegMetadata",
                        "add_metadata": True,
                    },
                    {
                        "key": "EmbedThumbnail",
                        "already_have_thumbnail": False,
                    },
                ],
            }
    elif urlObj["format"] == "audio":
        ydl_opts = {
                "paths": {"home": f"{DOWNLOAD_DIRECTORY}music"},
                "extract_audio": True,
                "format": "mp3/bestaudio/best",
                "writethumbnail": True,
                "embed-thumbnail": True,
                #'outtmpl': '%(playlist_index)02d-%(title)s.%(ext)s',
                "outtmpl": "%(channel)s/%(title)s.%(ext)s",
                "postprocessors": [
                    {"key": "FFmpegExtractAudio", "preferredcodec": "mp3"},
                    {"key": "EmbedThumbnail", "already_have_thumbnail": False},
                    {"key": "FFmpegMetadata", "add_metadata": True},
                ],
            }
    
    if "is_playlist" in urlObj:
        ydl_opts["outtmpl"] = (
            "%(playlist_title)s/%(playlist_index)02d-%(title)s.%(ext)s"
        )

    print(f"LLegue")
    print(f"Url Obj {urlObj}")


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urlObj["url"])
        
        
    