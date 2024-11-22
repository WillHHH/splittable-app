from supabase._async.client import AsyncClient
from datetime import datetime

from app.crud.base import CRUDBase
from app.schemas import TransactionParticipant, TransactionParticipantsCreate, TransactionParticipantUpdate
from app.schemas.auth import UserIn

class CRUDTransactionParticipant(CRUDBase[TransactionParticipant, TransactionParticipantsCreate, TransactionParticipantUpdate]):
    async def get_all(self, db: AsyncClient) -> list[TransactionParticipant]:
        return await super().get_all(db)
    
    async def get_transactions_by_group_id(self, db: AsyncClient, group_id: str) -> list[TransactionParticipant]:
        return await super().get_by_group_id(db, group_id=group_id)
    
    async def create(self, db: AsyncClient, *, obj_in: TransactionParticipantsCreate) -> TransactionParticipant:
        return await super().create(db, obj_in=obj_in)
    
    async def update(self, db: AsyncClient, *, obj_in: TransactionParticipantUpdate) -> TransactionParticipant:
        return await super().update(db, obj_in=obj_in)
    
    async def delete(self, db: AsyncClient, *, id: str) -> TransactionParticipant:
        return await super().delete(db, id=id)


transaction_participant = CRUDTransactionParticipant(TransactionParticipant)
