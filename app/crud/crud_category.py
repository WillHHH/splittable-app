from supabase._async.client import AsyncClient

from app.crud.base import CRUDBase
from app.schemas import Category, CategoryCreate, CategoryUpdate

class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    async def get_all(self, db: AsyncClient) -> list[Category]:
        return await super().get_all(db)

category = CRUDCategory(Category)
