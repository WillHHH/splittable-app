from typing import ClassVar
from app.schemas.base import CreateBase, InDBBase, ResponseBase, UpdateBase

# request
# Properties to receive on item creation
# in
class GroupCreate(CreateBase):
    pass

# Properties to receive on item update
# in
class GroupUpdate(UpdateBase):
    pass

# Properties to return to client
# curd model
# out
class Group(ResponseBase):
    table_name: ClassVar[str] = "Groups"
    group_name: str

# Properties properties stored in DB
class GroupInDB(InDBBase):
    pass
