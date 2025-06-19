from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import SHOP_LINEUP_PARAM


class ShopLineupParam(Base):
    __tablename__ = "shop_lineup_param"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int]
    soul_cost: Mapped[int]
    required_good: Mapped[int]
    quantity_flag: Mapped[int]
    qwcid: Mapped[int]
    initial_quantity: Mapped[int]
    shop_menu_type: Mapped[int]
    item_type: Mapped[int]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: SHOP_LINEUP_PARAM):
        self.id = id
        self.item_id = source.ItemID
        self.soul_cost = source.SoulCost
        self.required_good = source.RequiredGood
        self.quantity_flag = source.QuantityFlag
        self.qwcid = source.QWCID
        self.initial_quantity = source.InitialQuantity
        self.shop_menu_type = source.ShopMenuType
        self.item_type = source.ItemType
        self._pad0 = source._Pad0