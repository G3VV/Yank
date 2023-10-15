from quart import Quart, send_file
from util.spotify import start_token_thread
from util.download import start
from dotenv import load_dotenv
import threading
import re
import os

app = Quart("Yank")

load_dotenv()
port = os.environ.get("port")

@app.route('/track/<string:id>')
async def serve_audio(id):
    filename = await start(id)
    file_path = filename
    return await send_file(file_path, mimetype='audio/mpeg')

token_thread = threading.Thread(target=start_token_thread)
token_thread.start()

if __name__ == '__main__':
    app.run('0.0.0.0', port=port)