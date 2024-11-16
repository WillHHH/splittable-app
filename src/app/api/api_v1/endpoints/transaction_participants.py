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

@router.get("/all/{group_id}")
async def get_transactions_by_group_id(group_id: str, session: SessionDep) -> list[TransactionParticipant]:
    return await transaction_participant.get_transactions_by_group_id(session, group_id=group_id)

@router.post("/new")
async def create_transaction_participant(obj_in: TransactionParticipantsCreate, session: SessionDep) -> TransactionParticipant:
    return await transaction_participant.create(session, obj_in=obj_in)

@router.post("/new/batch")
async def create_transaction_participants(
    obj_in_list: list[TransactionParticipantsCreate], 
    session: SessionDep
) -> list[TransactionParticipant]:
    results = []
    for obj_in in obj_in_list:
        participant = await transaction_participant.create(session, obj_in=obj_in)
        results.append(participant)
    return results

# @router.put("/update")
# async def update_transaction(transaction_in: TransactionUpdate, session: SessionDep) -> Transaction:
#     return await transaction.update(session, obj_in=transaction_in)

@router.delete("/delete/batch")
async def delete_transaction_participants(
    ids: list[str], 
    session: SessionDep
) -> list[TransactionParticipant]:
    results = []
    for id in ids:
        participant = await transaction_participant.delete(session, id=id)
        results.append(participant)
    return results

@router.delete("/delete/{id}")
async def delete_transaction_participant(
    id: str, 
    session: SessionDep
) -> TransactionParticipant:
    return await transaction_participant.delete(session, id=id)
