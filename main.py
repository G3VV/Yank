from fastapi import FastAPI
from datetime import datetime
import uvicorn
from utils.download import downloadTrack as download_track_impl

app = FastAPI()

@app.get("/download/track")
async def downloadTrack(isrc: str = None, query: str = None):
    """
    Download a track using streamrip.
    
    Args:
        isrc: International Standard Recording Code (e.g., "USRC17607839")
        query: General search query (used if ISRC is not provided)
    
    Returns:
        JSON response with download status
    """
    result = await download_track_impl(isrc=isrc, query=query)
    result["timestamp"] = datetime.utcnow().isoformat()
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)