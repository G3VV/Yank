from util.spotify import spotify_isrc
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



def download_track(track_id, isrc):

    track = deezer.get_track(track_id)

    print(f"[{isrc}] Starting download")
    track["download"](download_dir, quality=track_formats.MP3_320, filename=isrc, with_lyrics=False, show_message=False)
    print(f"[{isrc}] Finished download")