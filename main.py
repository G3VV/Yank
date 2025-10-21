from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI(openapi_url=None)

@app.get("/download/track", description="Download a spotify track")
async def downloadTrack(id: str = None, q: str = None, query: str = None):
    q = query or q
    if q and id:
        return {"error": "Provide either 'id' or 'query', not both."}
    if not q and not id:
        return {"error": "Provide either 'id' or 'query'."}
    return {
        "id": id,
        "query": q,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/download/playlist", description="Download a spotify playlist")
async def downloadPlaylist(id: str = None):
    return {
        "id": id,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/", description="Got Root?")
async def root():
    def getRoutes():
        routes = {}
        for route in app.routes:
            if hasattr(route, "path"):
                routes[route.path] = str(route.description)
        return routes
    return {
        "message": "Hello, World!",
        "routes": getRoutes()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)