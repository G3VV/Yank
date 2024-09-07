![image](https://github.com/G3VV/Yank/assets/46306494/26eb50df-67f1-454a-ad3f-c286d54ebe61)


# Yank

Yank is a lightweight online spotify song and playlist downloader with easy setup.

## Features

- **Download Spotify Songs**: Yank enables you to download songs directly from Spotify.
- **Download Spotify Playlists**: Yank also allows you to download your entire playlist directly from Spotify.
- **Song Caching**: Yank caches songs to prevent unnecessary API calls and to speed up the download process.
- **High Quality Audio**: Yank downloads songs in high-quality audio formats for an optimal listening experience.
- **Metadata Retrieval**: Yank fetches metadata information like artist, album, and track name.

## Try it yourself!
1. Head to https://yank.g3v.co.uk/track/5EWFuo4ObEnfndc57sTuIo
2. Replace `5EWFuo4ObEnfndc57sTuIo` with a Spotify song ID and wait for it to download.

> Want to download a playlist?

1. Head to https://yank.g3v.co.uk/playlist/6V1papmDzwR16G3PBZEjTI
2. Replace `6V1papmDzwR16G3PBZEjTI` with a Spotify playlist ID and wait for it to download.
- Can take significantly longer depending on the playlist size.

## Prerequisites

- **Python**: Yank is written in Python and requires Python 3.6 or higher to run.
- **Spotify Developer Account**: You'll need to create a Spotify Developer account and obtain API credentials.
- **Deezer ARL**: You'll need your accounts ARL, usually stored in the cookies of the Deezer website.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/G3VV/yank.git
cd yank
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the `.env` file.
```env
deezer_arl=DEEZER_ACCOUNT_ARL # Your deezer account ARL cookie or https://www.youtube.com/watch?v=QEpZlWanx8g
spotify_id=SECRET_ID # spotify client id @ https://developer.spotify.com/dashboard
spotify_secret=SPOTIFY_SECRET # spotify client secret @ https://developer.spotify.com/dashboard

port = 7000 # Port to run the server on
ip = 0.0.0.0 # keep as 0.0.0.0 for automatic selection
```

## Usage

1. Open a terminal and navigate to the Yank directory:

```bash
cd /path/to/yank
```

2. Run Yank:

```bash
python index.py
```

3. Go to `http://localhost:7000/track/<track_id>`
> Replace `track_id` with the actual Spotify track ID.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details.

[![Star History Chart](https://api.star-history.com/svg?repos=G3VV/Yank&type=Date)](https://star-history.com/#G3VV/Yank&Date)
