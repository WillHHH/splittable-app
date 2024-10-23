from fastapi import APIRouter

from app.api.api_v1.endpoints import items, user, categories, groups, group_members, transactions, transaction_participants

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(groups.router, prefix="/groups", tags=["groups"])
api_router.include_router(group_members.router, prefix="/group_members", tags=["group_members"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
api_router.include_router(transaction_participants.router, prefix="/transaction_participants", tags=["transaction_participants"])
