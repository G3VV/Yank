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