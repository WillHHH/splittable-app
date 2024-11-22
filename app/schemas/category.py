from typing import ClassVar
from app.schemas.base import CreateBase, InDBBase, ResponseBase, UpdateBase

# request
# Properties to receive on item creation
# in
class CategoryCreate(CreateBase):
    pass

# Properties to receive on item update
# in
class CategoryUpdate(UpdateBase):
    pass

# Properties to return to client
# curd model
# out
class Category(ResponseBase):
    table_name: ClassVar[str] = "Categories"
    label: str
    color: str

# Properties properties stored in DB
class CategoryInDB(InDBBase):
    pass
