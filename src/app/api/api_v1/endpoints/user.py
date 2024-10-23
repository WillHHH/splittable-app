from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud import user
from app.schemas import User

router = APIRouter()

@router.get("/get-by-id/{id}")
async def read_user_by_id(id: str, session: SessionDep) -> User | None:
    return await user.get(session, id=id)
