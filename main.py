from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/title")
async def get_title(url: str):
    return "hello"
