from typing import ClassVar, Optional
from datetime import datetime
from app.schemas.base import CreateBase, InDBBase, ResponseBase, UpdateBase

# request
# Properties to receive on item creation
# in
class TransactionParticipantsCreate(CreateBase):
    id: str
    created_at: Optional[datetime]
    amount_owed: float
    transaction_id: str
    user_id: str

# Properties to receive on item update
# in
class TransactionUpdate(UpdateBase):
    id: Optional[str]
    created_at: Optional[datetime]
    amount_owed: Optional[float]
    transaction_id: Optional[str]
    user_id: Optional[str]

# Properties to return to client
# curd model
# out
class Transaction(ResponseBase):
    table_name: ClassVar[str] = "TransactionParticipants"
    amount_owed: float
    transaction_id: str
    user_id: str

# Properties properties stored in DB
class TransactionInDB(InDBBase):
    pass
