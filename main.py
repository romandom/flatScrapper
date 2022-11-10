import uvicorn
from fastapi import FastAPI
from flats.flats.spiders import flats
from scrapy.crawler import CrawlerProcess
from fastapi.responses import StreamingResponse

app = FastAPI()

path = "flats.html"


@app.get("/")
async def root():
    process = CrawlerProcess()
    process.crawl(flats.FlatSpider)
    process.start()

    def iter_file():
        with open(path, 'rb') as f:
            yield from f

    return StreamingResponse(iter_file(), media_type="text/html")

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
    print("running")


