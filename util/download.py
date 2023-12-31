from util.spotify import spotify_isrc, spotify_playlist
from util.deezer import get_deezer_track
from dotenv import load_dotenv
from pathlib import Path
from pydeezer import Deezer
from pydeezer import Downloader
from pydeezer.constants import track_formats
import asyncio
import httpx
import time
import base64
import os
import sys
import json
import shutil


load_dotenv()
download_dir = "./music/"
arl = os.environ.get("deezer_arl")

try:
    print("Logging into Deezer...")
    deezer = Deezer(arl=arl)
    print("Logged into Deezer")
except:
    print("Error logging into Deezer")


async def start(id):
    isrc = id
    try:

        try:
            track = await spotify_isrc(isrc)
        except Exception as e:
            print("Spotify token expired or couldn't find isrc")
            print(" ")
            print(e)
            return "none"

        if 'isrc' in track['external_ids']:
            isrc = track['external_ids']['isrc']
        else:
            isrc = "ISRC not available"
            print("Song not found")
            return "none"

        j = await get_deezer_track(isrc)
        pathfile = Path(f"./music/{isrc}.mp3")

        if pathfile.is_file():
            print(f"[{isrc}] Already cached")
            return pathfile
        else:
            print(f"[{isrc}] Not cached")
            try:
                track_id = j["id"]
            except:
                print("Couldn't find song on deezer")
                return "none"
            loop = asyncio.get_event_loop()
            download_track(track_id, isrc)
            return pathfile

    except Exception as e:
        print(f"{e} at line {sys.exc_info()[-1].tb_lineno}")
        return "none"

async def start_playlist(id):
    folder_to_zip = f'./music/{id}/'
    output_zip_file = f'./zip/{id}'
    def zip_folder(folder_path, output_path):
        print(f"[playlist] Zipping folder {folder_path} to {output_path}")

        shutil.make_archive(output_path, 'zip', folder_path)
        print(f"[playlist] Finished zipping folder {folder_path} to {output_path}")


    isrc = id
    try:
        if os.path.exists(folder_to_zip):
            return output_zip_file + ".zip"

        try:
            playlist_isrcs = await spotify_playlist(isrc)
        except Exception as e:
            print("Spotify token expired or couldn't find isrc")
            print(" ")
            print(e)
            return "none"

        deezer_ids = []

        for index in range(len(playlist_isrcs)):
            try:
                j = await get_deezer_track(playlist_isrcs[index])
                print(j["id"])
                deezer_ids.append(f'{j["id"]}')
            except:
                print("Couldn't find song on deezer")
                continue

        #return deezer_ids



        download_playlist(deezer_ids, id)

        zip_folder(folder_to_zip, output_zip_file)
        return output_zip_file + ".zip"

    except Exception as e:
        print(f"{e} at line {sys.exc_info()[-1].tb_lineno}")
        return "none"



def download_track(track_id, isrc):

    track = deezer.get_track(track_id)

    print(f"[{isrc}] Starting download")
    track["download"](download_dir, quality=track_formats.MP3_320, filename=isrc, with_lyrics=False, show_message=False)
    print(f"[{isrc}] Finished download")

def download_playlist(id_list, playlist_id):
    print(f"[playlist] Starting download")

    download_dir = f"./music/{playlist_id}/"
    downloader = Downloader(deezer, id_list, download_dir, quality=track_formats.MP3_320, concurrent_downloads=25)
    downloader.start()

    print(f"[playlist] Finished download")