from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import EQUIP_MTRL_SET_PARAM_ST


class EquipMtrlSetParamST(Base):
    __tablename__ = "equip_mtrl_set_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    upgrade_good: Mapped[int]
    upgrade_good2: Mapped[int]
    upgrade_good3: Mapped[int]
    upgrade_good4: Mapped[int]
    upgrade_good5: Mapped[int]
    upgrade_quantity: Mapped[int]
    upgrade_quantity2: Mapped[int]
    upgrade_quantity3: Mapped[int]
    upgrade_quantity4: Mapped[int]
    upgrade_quantity5: Mapped[int]
    disable_quantity_indicator: Mapped[bool]
    disable_quantity_indicator2: Mapped[bool]
    disable_quantity_indicator3: Mapped[bool]
    disable_quantity_indicator4: Mapped[bool]
    disable_quantity_indicator5: Mapped[bool]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: EQUIP_MTRL_SET_PARAM_ST):
        self.id = id
        self.upgrade_good = source.UpgradeGood
        self.upgrade_good2 = source.UpgradeGood2
        self.upgrade_good3 = source.UpgradeGood3
        self.upgrade_good4 = source.UpgradeGood4
        self.upgrade_good5 = source.UpgradeGood5
        self.upgrade_quantity = source.UpgradeQuantity
        self.upgrade_quantity2 = source.UpgradeQuantity2
        self.upgrade_quantity3 = source.UpgradeQuantity3
        self.upgrade_quantity4 = source.UpgradeQuantity4
        self.upgrade_quantity5 = source.UpgradeQuantity5
        self.disable_quantity_indicator = source.DisableQuantityIndicator
        self.disable_quantity_indicator2 = source.DisableQuantityIndicator2
        self.disable_quantity_indicator3 = source.DisableQuantityIndicator3
        self.disable_quantity_indicator4 = source.DisableQuantityIndicator4
        self.disable_quantity_indicator5 = source.DisableQuantityIndicator5
        self._pad0 = source._Pad0