import logging
from uvicorn import run

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.utils.core.log import Logger
from app.configs.config import load_config

from app.api.router_v1 import router as api_v1_router
from app.views.routes import router as view_router

app = FastAPI()

logger = Logger()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(view_router)
app.include_router(api_v1_router)

if __name__ == '__main__':
    config = load_config()
    run(
        "app.main:app", 
        host="0.0.0.0", 
        port=int(config['app']['port']), 
        log_level=config['logging']['level'].lower(), 
        workers=int(config['app']['workers']),
        reload=bool(config['app']['reload']),
        http="h11"
        )