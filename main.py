from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/twll")
async def twll(url: str):
    return "url"
