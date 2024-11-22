from supabase._async.client import AsyncClient

from app.crud.base import CRUDBase
from app.schemas import GroupMember, GroupMemberCreate, GroupMemberUpdate

class CRUDGroupMember(CRUDBase[GroupMember, GroupMemberCreate, GroupMemberUpdate]):
    async def get_members_by_group_id(self, db: AsyncClient, group_id: str) -> list[GroupMember]:
        return await super().get_by_group_id(db, group_id=group_id)

group_member = CRUDGroupMember(GroupMember)
