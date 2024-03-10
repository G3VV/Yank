from dotenv import load_dotenv
from pathlib import Path
import os
import httpx
import time
import base64

load_dotenv()
spotify_id = os.environ.get("spotify_id")
spotify_secret = os.environ.get("spotify_secret")
access_token = None

def start_token_thread():
    client_id = spotify_id
    client_secret = spotify_secret
    get_access_token(client_id, client_secret)

def get_access_token(client_id, client_secret):
    global access_token
    while True:
        try:
            client_creds = f"{client_id}:{client_secret}"
            client_creds_b64 = base64.b64encode(client_creds.encode())
            
            access_token_url = "https://accounts.spotify.com/api/token"
            headers = {"Authorization": f"Basic {client_creds_b64.decode()}"}
            data = {"grant_type": "client_credentials"}
            
            response = httpx.post(access_token_url, headers=headers, data=data)
            access_token = response.json()["access_token"]
        
        except Exception as e:
            print(f"Error retrieving access token: {str(e)}")
        time.sleep(600)

async def spotify_isrc(track_id):
                endpoint = f"https://api.spotify.com/v1/tracks/{track_id}"
                headers = {
                    "Authorization": f"Bearer {access_token}",
                }
                response = httpx.get(endpoint, headers=headers)
                track = response.json()
                return track

async def spotify_playlist(playlist_id):
    endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    song_isrcs = []
    offset = 0
    limit = 100
    while True:
        params = {
            "offset": offset,
            "limit": limit
        }
        response = httpx.get(endpoint, headers=headers, params=params)
        playlist = response.json()
        for i in playlist['items']:
            try:
                song_isrcs.append(i['track']['external_ids']['isrc'])
            except:
                pass
        offset += limit
        if offset >= playlist['total']:
            break
    return song_isrcs
