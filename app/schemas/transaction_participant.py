from typing import ClassVar, Optional
from datetime import datetime
from app.schemas.base import CreateBase, InDBBase, ResponseBase, UpdateBase

# request
# Properties to receive on item creation
# in
class TransactionParticipantsCreate(CreateBase):
    table_name: ClassVar[str] = "TransactionParticipants"
    id: str
    created_at: Optional[datetime] = datetime.now()
    amount_owed: float
    transaction_id: str
    user_id: str
    is_payer: bool
    total: float
    group_id: str

# Properties to receive on item update
# in
class TransactionParticipantUpdate(UpdateBase):
    table_name: ClassVar[str] = "TransactionParticipants"
    id: str
    created_at: Optional[datetime] = datetime.now()
    amount_owed: Optional[float] = None
    transaction_id: Optional[str] = None
    user_id: Optional[str] = None

# Properties to return to client
# curd model
# out
class TransactionParticipant(ResponseBase):
    table_name: ClassVar[str] = "TransactionParticipants"
    created_at: datetime
    amount_owed: float
    transaction_id: str
    user_id: str    
    is_payer: bool
    total: float

# Properties properties stored in DB
class TransactionParticipantInDB(InDBBase):
    pass
