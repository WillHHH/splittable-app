from fastapi import APIRouter, Query

from app.api.deps import SessionDep
from app.crud import transaction_participant
from app.schemas import TransactionParticipant, TransactionParticipantsCreate, TransactionParticipantUpdate

router = APIRouter()

@router.get("/all")
async def get_all(session: SessionDep) -> list[TransactionParticipant]:
    return await transaction_participant.get_all(session)

@router.get("/all/date-range")
async def get_transactions_by_date_range(
    session: SessionDep,
    group_id: str = Query(..., description="group id"),
    start_date: str = Query(..., description="start date"),
    end_date: str = Query(..., description="end date"),
) -> list[TransactionParticipant]:
    return await transaction_participant.get_by_date_range(session, group_id, start_date, end_date)

@router.post("/new")
async def create_transaction_participant(obj_in: TransactionParticipantsCreate, session: SessionDep) -> TransactionParticipant:
    return await transaction_participant.create(session, obj_in=obj_in)

# @router.put("/update")
# async def update_transaction(transaction_in: TransactionUpdate, session: SessionDep) -> Transaction:
#     return await transaction.update(session, obj_in=transaction_in)

# @router.delete("/delete/{id}")
# async def delete_transaction(id: str, session: SessionDep) -> Transaction:
#     return await transaction.delete(session, id=id)
