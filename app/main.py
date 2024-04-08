from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.utils.core.log import Logger

from app.api.router_v1 import router as api_v1_router
from app.views.routes import router as view_router

logger = Logger()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(view_router)
app.include_router(api_v1_router)