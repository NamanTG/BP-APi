from fastapi import FastAPI
from aiohttp import ClientSession

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/twll")
async def twll(url: str):
    s = ClientSession()
    r = await s.get(url, allow_redirects=False)
    return await r.text()
