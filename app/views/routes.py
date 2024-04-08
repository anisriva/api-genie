from asyncio import sleep
from datetime import datetime

from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.utils.product_card_generator import gen_product_card_item_list
from app.utils.core.text_generator import async_generate_lorem_ipsum

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home(
                request: Request, 
                ):
   # Template generation accounted prior delay sleep
    template =  templates.TemplateResponse(
                        name="index.html", 
                        context={
                                "request": request 
                                })

    return template

@router.get("/products", response_class=HTMLResponse)
async def product_simulate_view(
                request: Request, 
                delay_ms: int = Query(0, alias="delay_ms"), 
                payload_size_kb: int = Query(10, alias="payload_size_kb")
                ):
    # Record start time
    start_time = datetime.now()
    # Convert KB to bytes for the payload generation
    requested_bytes = payload_size_kb * 1024
    product_card_items = await gen_product_card_item_list(requested_bytes)

    # Template generation accounted prior delay sleep
    template =  templates.TemplateResponse(
                        name="product.html", 
                        context={
                                "request": request, 
                                "products" : product_card_items,
                                "email" : "animesh.srivastava@lowes.com"
                                })
    # Wait for the remaining time
    elapsed_time = (datetime.now() - start_time).total_seconds() * 1000
    remaining_time = max(0, delay_ms - elapsed_time) / 1000
    await sleep(remaining_time)

    return template

@router.get("/text", response_class=HTMLResponse)
async def text_simulate_view(
                request: Request,
                delay_ms : int = Query(0, alias="delay_ms"),
                payload_size_kb : int = Query(10, alaias="payload_size_kb")
                ):
        # Record start time
        start_time = datetime.now()
        # Convert KB to bytes for the text generation
        requested_bytes = payload_size_kb * 1024
        plain_text = await async_generate_lorem_ipsum(requested_bytes)
        template = templates.TemplateResponse(
                                name="plain.html",
                                context={
                                     "request" : request,
                                     "title" : "Simulate - text",
                                     "plain_text" : plain_text,
                                })
        # Wait for the remaining time
        elapsed_time = (datetime.now() - start_time).total_seconds() * 1000
        remaining_time = max(0, delay_ms - elapsed_time) / 1000
        await sleep(remaining_time)
        return template
