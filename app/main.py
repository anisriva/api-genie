import asyncio
from datetime import datetime

from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.utils.core.log import Logger
# from app.utils.core.text_generator import generate_lorem_ipsum_payload
from app.utils.product_card_generator import gen_product_card_item_list

logger = Logger()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/debug", response_class=HTMLResponse)
async def product_simulate_response(
                request: Request, 
                ):
   # Template generation accounted prior delay sleep
    template =  templates.TemplateResponse(
                        name="base-debug.html", 
                        context={
                                "request": request, 
                                "title":"Api Genie", 
                                })
    # return template
    return template

@app.get("/product", response_class=HTMLResponse)
async def product_simulate_response(
                request: Request, 
                delay_ms: int = Query(0, alias="delay_ms"), 
                payload_size_kb: int = Query(10, alias="payload_size_kb")
                ):
    # Record start time
    start_time = datetime.now()
    # Convert KB to bytes for the payload generation
    requested_bytes = payload_size_kb * 1024
    product_card_items = gen_product_card_item_list(requested_bytes)

    # Template generation accounted prior delay sleep
    template =  templates.TemplateResponse(
                        name="product.html", 
                        context={
                                "request": request, 
                                "products" : product_card_items,
                                "year" : str(datetime.now().year),
                                "email" : "animesh.srivastava@lowes.com"
                                })
    # Wait for the remaining time
    elapsed_time = (datetime.now() - start_time).total_seconds() * 1000
    remaining_time = max(0, delay_ms - elapsed_time) / 1000
    asyncio.sleep(remaining_time)
    # return template
    return template