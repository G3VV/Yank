from deezspot.deezloader import DeeLogin

deezer = DeeLogin(arl='arl here', tags_separator=" / ")

async def downloadTrack(id: str = None, query: str = None):
    deezer.download_trackdee(
        link_track='https://www.deezer.com/track/3473370681',
        output_dir='./tracks',
        quality_download='MP3_128',
        recursive_quality=False,
        recursive_download=False
    )
    