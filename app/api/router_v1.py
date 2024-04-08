from fastapi import APIRouter

from app.api.v1.simulate_payload import router as simulate_router

router = APIRouter()

router.include_router(simulate_router, prefix='/api/v1', tags=["simulate-payload"])