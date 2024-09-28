from fastapi import APIRouter

from app.api.api_v1.endpoints import items, transactions

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
