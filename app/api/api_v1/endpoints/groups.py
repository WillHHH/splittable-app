from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud import group
from app.schemas import Group

router = APIRouter()

@router.get("/all")
async def get_all(session: SessionDep) -> list[Group]:
    return await group.get_all(session)