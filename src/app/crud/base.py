import json
from typing import Generic, TypeVar

from supabase_py_async import AsyncClient

from app.schemas.auth import UserIn
from app.schemas.base import CreateBase, ResponseBase, UpdateBase

ModelType = TypeVar("ModelType", bound=ResponseBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=CreateBase)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=UpdateBase)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    async def get(self, db: AsyncClient, *, id: str) -> ModelType | None:
        """get by table_name by id"""
        data, count = (
            await db.table(self.model.table_name).select("*").eq("id", id).execute()
        )
        _, got = data
        return self.model(**got[0]) if got else None

    async def get_all(self, db: AsyncClient) -> list[ModelType]:
        """get all by table_name"""
        data, count = await db.table(self.model.table_name).select("*").execute()
        _, got = data
        return [self.model(**item) for item in got]
    
    async def get_by_date_range(
        self, 
        db: AsyncClient, 
        group_id: str,
        start_date: str, 
        end_date: str
    ) -> list[ModelType]:
        """get all by date range"""
        data, count = (
            await db.table(self.model.table_name)
            .select("*")
            .eq("group_id", group_id)
            .gte("created_at", start_date)
            .lte("created_at", end_date)
            .order("created_at", desc=True)
            .execute()
        )
        _, got = data
        return [self.model(**item) for item in got]

    async def get_multi_by_owner(
        self, db: AsyncClient, *, user: UserIn
    ) -> list[ModelType]:
        """get by owner,use it  if rls failed to use"""
        data, count = (
            await db.table(self.model.table_name)
            .select("*")
            .eq("user_id", user.id)
            .execute()
        )
        _, got = data
        return [self.model(**item) for item in got]
    
    async def get_by_group_id(
        self, db: AsyncClient, *, group_id: str
    ) -> list[ModelType]:
        """get by owner,use it  if rls failed to use"""
        data, count = (
            await db.table(self.model.table_name)
            .select("*")
            .eq("group_id", group_id)
            .order("created_at", desc=True)
            .execute()
        )
        _, got = data
        return [self.model(**item) for item in got]

    async def create(self, db: AsyncClient, *, obj_in: CreateSchemaType) -> ModelType:
        """create by CreateSchemaType"""
        data, count = (
            await db.table(self.model.table_name).insert(json.loads(obj_in.model_dump_json())).execute()
        )
        _, created = data
        return self.model(**created[0])

    async def update(self, db: AsyncClient, *, obj_in: UpdateSchemaType) -> ModelType:
        """update by UpdateSchemaType"""
        update_data = json.loads(obj_in.model_dump_json(exclude_unset=True, exclude_none=True))
        
        target_id = update_data.pop("id", None)
        if id is None:
            raise ValueError("ID must be provided for update operation")

        data, count = (
            await db.table(self.model.table_name)
            .update(update_data)
            .eq("id", target_id)
            .execute()
        )
        _, updated = data
        return self.model(**updated[0])

    async def delete(self, db: AsyncClient, *, id: str) -> ModelType:
        """remove by UpdateSchemaType"""
        data, count = (
            await db.table(self.model.table_name).delete().eq("id", id).execute()
        )
        _, deleted = data
        return self.model(**deleted[0])
