from quart import Quart, send_file
from quart_cors import cors
from util.spotify import start_token_thread
from util.download import start, start_playlist
from util.statistics import totalCaches, totalSongs, totalPlaylists, totalSongData
from dotenv import load_dotenv
import threading
import re
import os
import json

app = Quart(__name__)
app = cors(app, allow_origin="*")

load_dotenv()
port = os.environ.get("PORT")
ip = os.environ.get("IP")

@app.route('/track/<string:id>')
async def serve_audio(id):
    try:
        filename = await start(id)
        return await send_file(filename, mimetype='audio/mpeg'), 200
    except:
        return {
            "failed": True,
            "message": "Song not found"
        }, 404

@app.route('/playlist/<string:id>')
async def serve_playlist(id):
    try:
        filename = await start_playlist(id)
        return await send_file(filename, as_attachment=True, attachment_filename=f'{id}.zip', mimetype='application/zip'), 200
    except:
        return {
            "failed": True,
            "message": "Playlist not found"
        }, 404

@app.route("/stats")
async def stats():
    return {
        "failed": False,
        "data": {
            "total": await totalCaches(),
            "songs": await totalSongs(),
            "caches": await totalSongData(),
            "playlists": await totalPlaylists()
        }
    }

@app.route('/')
async def serve_index():
    return {
        "message": "Online",
        "github": "https://github.com/g3vv/yank",
        "routes": {
            "track": "/track/{song_id}",
            "playlist": "/playlist/{playlist_id}",
            "stats": "/stats"
        }
    }

token_thread = threading.Thread(target=start_token_thread)
token_thread.start()

if __name__ == '__main__':
    app.run(ip, port=port)
