import asyncio
import os
from pathlib import Path
from streamrip import Config
from streamrip.client import DeezerClient
from streamrip.rip.main import Main

async def downloadTrack(isrc: str = None, query: str = None):
    """
    Download a track using streamrip.
    
    Args:
        isrc: International Standard Recording Code for the track
        query: General search query (if ISRC is not provided)
    
    Returns:
        dict: Download result information
    """
    if not isrc and not query:
        return {
            "status": "error",
            "message": "Either ISRC or query must be provided"
        }
    
    try:
        # Get the default config path
        config_path = os.path.expanduser("~/.config/streamrip/config.toml")
        
        # Initialize streamrip
        config = Config(config_path)
        main = Main(config)
        
        # Use ISRC search if provided
        if isrc:
            # Format ISRC for Deezer search: isrc:"CODE"
            search_query = f'isrc:"{isrc}"'
            
            # Search for the track using Deezer (most reliable for ISRC)
            client = await main.get_logged_in_client("deezer")
            search_results = await client.search("track", search_query, limit=1)
            
            if not search_results or not search_results[0].get("data"):
                return {
                    "status": "error",
                    "message": f"No track found with ISRC: {isrc}"
                }
            
            # Get the first track ID
            track_data = search_results[0]["data"][0]
            track_id = str(track_data["id"])
            
            # Add track for download
            await main.add_by_id("deezer", "track", track_id)
        else:
            # Use general search query
            await main.search_take_first("deezer", "track", query)
        
        # Download all pending items
        await main.resolve()
        
        return {
            "status": "success",
            "message": "Track download completed",
            "isrc": isrc,
            "query": query
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "isrc": isrc,
            "query": query
        }
