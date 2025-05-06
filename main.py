from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI()

@app.get("/download/track")
async def downloadTrack(id: str = None, query: str = None):
    return {
        "id": id,
        "query": query,
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)