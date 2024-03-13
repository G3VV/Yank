import os

song_directory = "music"
playlist_directory = "zip"

async def totalCaches():
    return len(os.listdir(song_directory)) + len(os.listdir(playlist_directory))

async def totalSongs():
    return len(os.listdir(song_directory))

async def totalPlaylists():
    return len(os.listdir(playlist_directory))