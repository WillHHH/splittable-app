from supabase_py_async import AsyncClient
from datetime import datetime

from app.crud.base import CRUDBase
from app.schemas import Transaction, TransactionCreate, TransactionUpdate
from app.schemas.auth import UserIn

class CRUDTransaction(CRUDBase[Transaction, TransactionCreate, TransactionUpdate]):
    async def get_all(self, db: AsyncClient) -> list[Transaction]:
        return await super().get_all(db)
    
    async def get_by_date_range(
        self, 
        db: AsyncClient, 
        start_date: str, 
        end_date: str
    ) -> list[Transaction]:
        return await super().get_by_date_range(db, start_date, end_date)
    
    async def create(self, db: AsyncClient, *, obj_in: TransactionCreate) -> Transaction:
        return await super().create(db, obj_in=obj_in)
    
    async def update(self, db: AsyncClient, *, obj_in: TransactionUpdate) -> Transaction:
        return await super().update(db, obj_in=obj_in)
    
    async def delete(self, db: AsyncClient, *, id: str) -> Transaction:
        return await super().delete(db, id=id)


transaction = CRUDTransaction(Transaction)