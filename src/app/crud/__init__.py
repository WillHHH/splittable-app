"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 07/01/2024
@Description  :
"""

from .crud_item import item
from .crud_user import user
from .crud_group import group
from .crud_category import category
from .crud_group_member import group_member
from .crud_transaction import transaction
from .crud_transaction_participant import transaction_participant

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
