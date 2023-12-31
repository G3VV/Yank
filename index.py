from quart import Quart, send_file
from util.spotify import start_token_thread
from util.download import start, start_playlist
from dotenv import load_dotenv
import threading
import re
import os
import json

app = Quart(__name__)

load_dotenv()
port = os.environ.get("port")

@app.route('/track/<string:id>')
async def serve_audio(id):
    filename = await start(id)
    return await send_file(filename, mimetype='audio/mpeg')

@app.route('/')
async def serve_index():
    return "online"

@app.route('/playlist/<string:id>')
async def serve_playlist(id):
    filename = await start_playlist(id)
    return await send_file(filename, as_attachment=True, attachment_filename='playlist.zip', mimetype='application/zip')

token_thread = threading.Thread(target=start_token_thread)
token_thread.start()

if __name__ == '__main__':
    app.run('0.0.0.0', port=port)