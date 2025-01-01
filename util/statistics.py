import os

song_directory = "music"
playlist_directory = "zip"
cache_directory = "cache"

async def totalCaches():
    song_count = len(os.listdir(song_directory)) if os.path.exists(song_directory) else 0
    playlist_count = len(os.listdir(playlist_directory)) if os.path.exists(playlist_directory) else 0
    cache_count = len(os.listdir(cache_directory)) if os.path.exists(cache_directory) else 0
    return song_count + playlist_count + cache_count

async def totalSongs():
    return len(os.listdir(song_directory)) if os.path.exists(song_directory) else 0

async def totalPlaylists():
    return len(os.listdir(playlist_directory)) if os.path.exists(playlist_directory) else 0

async def totalSongData():
    return len(os.listdir(cache_directory)) if os.path.exists(cache_directory) else 0

async def totalStorage():
    song_size = sum(os.path.getsize(f"{song_directory}/{f}") for f in os.listdir(song_directory)) if os.path.exists(song_directory) else 0
    playlist_size = sum(os.path.getsize(f"{playlist_directory}/{f}") for f in os.listdir(playlist_directory)) if os.path.exists(playlist_directory) else 0
    cache_size = sum(os.path.getsize(f"{cache_directory}/{f}") for f in os.listdir(cache_directory)) if os.path.exists(cache_directory) else 0
    return song_size + playlist_size + cache_size

async def songStorage():
    song_size = sum(os.path.getsize(f"{song_directory}/{f}") for f in os.listdir(song_directory)) if os.path.exists(song_directory) else 0
    return song_size

async def playlistStorage():
    playlist_size = sum(os.path.getsize(f"{playlist_directory}/{f}") for f in os.listdir(playlist_directory)) if os.path.exists(playlist_directory) else 0
    return playlist_size

async def cacheStorage():
    cache_size = sum(os.path.getsize(f"{cache_directory}/{f}") for f in os.listdir(cache_directory)) if os.path.exists(cache_directory) else 0
    return cache_size