from fastapi import APIRouter, Query
from datetime import datetime

from app.api.deps import CurrentUser, SessionDep
from app.crud import transaction
from app.schemas import Transaction, TransactionCreate, TransactionUpdate

router = APIRouter()

@router.get("/all")
async def get_all(session: SessionDep) -> list[Transaction]:
    return await transaction.get_all(session)

@router.get("/all/date-range")
async def get_transactions_by_date_range(
    session: SessionDep,
    start_date: str = Query(..., description="start date"),
    end_date: str = Query(..., description="end date"),
) -> list[Transaction]:
    return await transaction.get_by_date_range(session, start_date, end_date)

@router.post("/new")
async def create_transaction(transaction_in: TransactionCreate, session: SessionDep) -> Transaction:
    return await transaction.create(session, obj_in=transaction_in)

@router.put("/update")
async def update_transaction(transaction_in: TransactionUpdate, session: SessionDep) -> Transaction:
    return await transaction.update(session, obj_in=transaction_in)

@router.delete("/delete/{id}")
async def delete_transaction(id: str, session: SessionDep) -> Transaction:
    return await transaction.delete(session, id=id)
