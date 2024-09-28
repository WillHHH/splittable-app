from typing import ClassVar, Optional
from datetime import datetime
from app.schemas.base import CreateBase, InDBBase, ResponseBase, UpdateBase

# request
# Properties to receive on item creation
# in
class TransactionCreate(CreateBase):
    table_name: ClassVar[str] = "Transactions"
    created_at: Optional[datetime] = datetime.now()
    amount: float
    description: str
    updated_at: Optional[datetime] = None
    created_by: str

# Properties to receive on item update
# in
class TransactionUpdate(UpdateBase):
    table_name: ClassVar[str] = "Transactions"
    id: str
    amount: Optional[float] = None
    description: Optional[str] = None
    updated_at: Optional[datetime] = datetime.now()
    created_by: Optional[str] = None

# Properties to return to client
# curd model
# out
class Transaction(ResponseBase):
    table_name: ClassVar[str] = "Transactions"
    amount: float
    updated_at: Optional[datetime]
    description: str
    created_by: str

# Properties properties stored in DB
class TransactionInDB(InDBBase):
    pass
