import json
import os
import sys
import shutil
import warnings
from pathlib import Path

from cryptography.utils import CryptographyDeprecationWarning
from dotenv import load_dotenv
from pydeezer import Deezer, Downloader
from pydeezer.constants import track_formats
from util.spotify import spotify_isrc, spotify_playlist
from util.deezer import get_deezer_track

warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
load_dotenv()

arl = os.environ.get("deezer_arl")
DOWNLOAD_DIR = "./music/"
CACHE_DIR = "./cache/"
ZIP_DIR = "./zip/"

try:
    print("Logging into Deezer...")
    deezer = Deezer(arl=arl)
    print("Logged into Deezer")
except Exception as e:
    print("Error logging into Deezer, possibly ratelimited? make sure your ARL is correct.")
    sys.exit(1)

def delete_temporary_folder(folder_path):
    print(f"Deleting temporary folder {folder_path}")
    shutil.rmtree(folder_path)
    print("Finished deleting temporary folder")

def delete_lyrics(folder_path):
    print(f"Deleting lyrics from {folder_path}")
    for filename in os.listdir(folder_path):
        if filename.endswith(".lrc"):
            os.remove(os.path.join(folder_path, filename))
    print("Finished deleting lyrics")

def zip_folder(folder_path, output_path):
    print(f"Zipping folder {folder_path} to {output_path}")
    shutil.make_archive(output_path, 'zip', folder_path)
    print("Finished zipping folder")

def download_track(track_id, isrc):
    track = deezer.get_track(track_id)
    print(f"[{isrc}] Starting download")
    track["download"](DOWNLOAD_DIR, quality=track_formats.MP3_320, filename=isrc, with_lyrics=False, show_message=False)
    print(f"[{isrc}] Finished download")

def download_playlist(id_list, playlist_id):
    print("Starting playlist download")
    download_dir = f"./music/{playlist_id}/"
    downloader = Downloader(deezer, id_list, download_dir, quality=track_formats.MP3_320, concurrent_downloads=25)
    downloader.start()
    print("Finished playlist download")

async def start(id):
    isrc = id
    try:
        try:
            track = await spotify_isrc(isrc)
        except Exception as e:
            print("Spotify token expired or couldn't find ISRC")
            print(e)
            return "none"

        isrc = track.get('external_ids', {}).get('isrc', "ISRC not available")
        if isrc == "ISRC not available":
            print("Song not found")
            return "none"

        cache_file = Path(f"./cache/{isrc}.json")
        if cache_file.is_file():
            print(f"[{isrc}] Found data in cache")
            with open(cache_file, 'r') as f:
                j = json.load(f)
        else:
            print(f"[{isrc}] Not found in data cache, fetching from Deezer")
            j = await get_deezer_track(isrc)
            with open(cache_file, 'w') as f:
                json.dump(j, f)

        pathfile = Path(f"./music/{isrc}.mp3")
        if pathfile.is_file():
            print(f"[{isrc}] Already cached")
            return pathfile

        print(f"[{isrc}] Not cached")
        track_id = j.get("id")
        if not track_id:
            print("Couldn't find song on Deezer")
            return "none"

        download_track(track_id, isrc)
        return pathfile

    except Exception as e:
        print(f"{e} at line {sys.exc_info()[-1].tb_lineno}")
        return "none"

async def start_playlist(id):
    folder_to_zip = f'./music/{id}/'
    output_zip_file = f'./zip/{id}'
    pathfile = Path(f"./zip/{id}.zip")
    isrc = id

    if pathfile.is_file():
        print(f"[playlist] Already cached")
        return output_zip_file + ".zip"

    try:
        playlist_isrcs = await spotify_playlist(isrc)
    except Exception as e:
        print("Spotify token expired or couldn't find ISRC")
        print(e)
        return "none"

    deezer_ids = []
    for isrc in playlist_isrcs:
        try: # this is to stop deezer blocking requests
            cache_file = Path(f"./cache/{isrc}.json")
            if cache_file.is_file():
                print(f"[{isrc}] Found in data cache")
                with open(cache_file, 'r') as f:
                    j = json.load(f)
            else:
                print(f"[{isrc}] Not found in data cache, fetching from Deezer")
                j = await get_deezer_track(isrc)
                with open(cache_file, 'w') as f:
                    json.dump(j, f)
            deezer_ids.append(str(j["id"]))
        except Exception as e:
            print(f"Couldn't find song on Deezer ({isrc}) {e}")
            continue

    print(f"Found {len(deezer_ids)}/{len(playlist_isrcs)} songs")
    download_playlist(deezer_ids, id)
    delete_lyrics(folder_to_zip)
    zip_folder(folder_to_zip, output_zip_file)
    delete_temporary_folder(folder_to_zip)
    return output_zip_file + ".zip"
