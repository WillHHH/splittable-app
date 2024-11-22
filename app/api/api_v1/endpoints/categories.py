from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud import category
from app.schemas import Category

router = APIRouter()

@router.get("/all")
async def get_all(session: SessionDep) -> list[Category]:
    return await category.get_all(session)