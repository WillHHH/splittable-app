from supabase._async.client import AsyncClient

from app.crud.base import CRUDBase
from app.schemas import Group, GroupCreate, GroupUpdate

class CRUDGroup(CRUDBase[Group, GroupCreate, GroupUpdate]):
    async def get_all(self, db: AsyncClient) -> list[Group]:
        return await super().get_all(db)

group = CRUDGroup(Group)
