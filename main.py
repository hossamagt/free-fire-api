from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import aiohttp

app = FastAPI()

API_URL = "https://fred-fire-info-gj.vercel.app/player-info"
API_PASSWORD = "hossamdev"  # غيّرها كما تحب

@app.get("/")
async def get_player_info(uid: str, region: str, password: str):
    if password != API_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid password")

    url = f"{API_URL}?uid={uid}&region={region}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return JSONResponse(status_code=resp.status, content={"error": "Failed to fetch player info."})
            return await resp.json()
