from asyncio import sleep
from datetime import datetime

from fastapi import APIRouter, Request, Query

from app.utils.core.text_generator import async_generate_lorem_ipsum

router = APIRouter()

@router.get("/simulate-text", status_code=200)
async def generate_text_api(
                request : Request,
                delay_ms : int = Query(0, alias="delay_ms"),
                payload_size_kb : int = Query(10, alias="payload_size_kb")
                ):
    # Record the start time
    start_time = datetime.now()
    # Convert KB to bytes for the text generation
    requested_bytes = payload_size_kb * 1024
    # Generate text
    requested_text = await async_generate_lorem_ipsum(requested_bytes)
    # Wait for the remaining time
    elapsed_time = (datetime.now()- start_time).total_seconds() * 1000
    remaining_time = max(0, delay_ms - elapsed_time) / 1000
    await sleep(remaining_time)
    return {
        "delay_ms" : delay_ms,
        "request_bytes" : requested_bytes,
        "generated_text" : requested_text
    }
