from typing import ClassVar
from app.schemas.base import CreateBase, InDBBase, ResponseBase, UpdateBase

# request
# Properties to receive on item creation
# in
class GroupMemberCreate(CreateBase):
    pass

# Properties to receive on item update
# in
class GroupMemberUpdate(UpdateBase):
    pass

# Properties to return to client
# curd model
# out
class GroupMember(ResponseBase):
    table_name: ClassVar[str] = "GroupMembers"
    user_id: str
    avatar_url: str | None
    name: str
    group_id: str

# Properties properties stored in DB
class GroupMemberInDB(InDBBase):
    pass
