from typing import Optional

from fastapi import FastAPI

import asyncio
import logging

logger=logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    logger.info("Hello")
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None, delay: Optional[int]=0):
    # Add some delay if specified
    
    if delay>0:
        logger.info(f"[{item_id}:{q}] Sleeping for {delay}")
        await asyncio.sleep(delay)
        logger.info(f"[{item_id}/{q}] Slept for {delay}")
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO,force=True)

    import uvicorn, os
    
    uvicornFmter=uvicorn.logging.DefaultFormatter(use_colors=True,fmt='%(levelprefix)s %(message)s')

    strh=logging.StreamHandler()
    strh.setFormatter(uvicornFmter)
    logger.addHandler(strh)
    logger.setLevel(logging.INFO)
    logger.info("Logging info")
    logger.error("Logging error")

    api_port=os.environ.get('API_PORT','8002')

    uvicorn.run(app, host="0.0.0.0", port=int(api_port))