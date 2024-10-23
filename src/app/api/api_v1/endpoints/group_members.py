from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud import group_member
from app.schemas import GroupMember

router = APIRouter()

@router.get("/all/{group_id}")
async def get_members_by_group_id(group_id: str, session: SessionDep) -> list[GroupMember]:
    return await group_member.get_members_by_group_id(session, group_id=group_id)