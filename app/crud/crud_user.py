from supabase._async.client import AsyncClient

from app.crud.base import CRUDBase
from app.schemas import User, UserCreate, UserUpdate

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def __init__(self):
        super().__init__(User)

    async def get(self, db: AsyncClient, *, id: str) -> User | None:
        data = (await db.auth.admin.get_user_by_id(id))
        print(data.user.user_metadata)
        if data.user.user_metadata:
            user_data = {
                "id": id,
                "created_at": data.user.created_at.isoformat(),
                **data.user.user_metadata
            }
            return User(**user_data)
        return None

user = CRUDUser()