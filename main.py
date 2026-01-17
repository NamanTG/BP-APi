from fastapi import FastAPI
from playwright.async_api import async_playwright

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/title")
async def get_title(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = await browser.new_page()
        await page.goto(url, timeout=30000)
        title = await page.title()
        await browser.close()

    return {
        "url": url,
        "title": title
    }
