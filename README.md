![image](https://github.com/G3VV/Yank/assets/46306494/b71939a5-27c7-449e-9913-6a710554dc2c)

# Yank

Yank is a lightweight online spotify song downloader with easy setup.

## Features

- **Download Spotify Songs**: Yank enables you to download songs directly from Spotify.
- **Song Caching**: Yank caches songs to prevent unnecessary API calls and to speed up the download process.
- **High Quality Audio**: Yank downloads songs in high-quality audio formats for an optimal listening experience.
- **Metadata Retrieval**: Yank fetches metadata information like artist, album, and track name.

## Prerequisites

- **Python**: Yank is written in Python and requires Python 3.6 or higher to run.
- **Spotify Developer Account**: You'll need to create a Spotify Developer account and obtain API credentials.
- **Deezer ARL**: You'll need your accounts ARL, usually stored in the cookies of the Deezer website.

## Try it yourself!
1. Head to https://yank.g3v.co.uk/track/7iClDFej8POrB7757pJsd7
2. Replace `7iClDFej8POrB7757pJsd7` with a Spotify song ID and wait for it to download.

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
```
deezer_arl=DEEZER_ACCOUNT_ARL # Your deezer account ARL cookie or https://www.youtube.com/watch?v=QEpZlWanx8g
spotify_id=SECRET_ID # spotify client id @ https://developer.spotify.com/dashboard
spotify_secret=SPOTIFY_SECRET # spotify client secret @ https://developer.spotify.com/dashboard

port = 7000 # Port to run the server on
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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
