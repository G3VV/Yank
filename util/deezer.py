from dotenv import load_dotenv
import os
import httpx

load_dotenv()
arl = os.environ.get("deezer_arl")

headers = {"Accept-Encoding": "gzip, deflate"}
cookies = {'arl': arl}

async def get_deezer_track(isrc):
        response = httpx.get('https://api.deezer.com/2.0/track/isrc:' + isrc, cookies=cookies, headers=headers)
        return response.json()