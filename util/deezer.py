import asyncio
import os

from dotenv import load_dotenv
import httpx

load_dotenv()
arl = os.environ.get("deezer_arl")

headers = {"Accept-Encoding": "gzip, deflate"}
cookies = {'arl': arl}


async def get_deezer_track(isrc):
    while True:
        response = httpx.get(
            'https://api.deezer.com/2.0/track/isrc:' + isrc,
            cookies=cookies,
            headers=headers,
        )
        if response.status_code == 200:
            return response.json()
        else:
            await asyncio.sleep(15)
