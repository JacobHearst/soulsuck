from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import EQUIP_PARAM_ACCESSORY_ST


class EquipParamAccessoryST(Base):
    __tablename__ = "equip_param_accessory_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    special_effect: Mapped[int]
    sfx_variation: Mapped[int]
    weight: Mapped[float]
    behavior: Mapped[int]
    basic_cost: Mapped[int]
    frampt_sell_value: Mapped[int]
    sort_index: Mapped[int]
    qwcid: Mapped[int]
    equipment_model: Mapped[int]
    menu_icon: Mapped[int]
    shop_level: Mapped[int]
    achievement_contribution_id: Mapped[int]
    achievement_unlock_id: Mapped[int]
    equipment_model_category: Mapped[int]
    equipment_model_gender: Mapped[int]
    accessory_category: Mapped[int]
    reference_type: Mapped[int]
    special_effect_category: Mapped[int]
    _pad0: Mapped[bytes]
    vagrant_item_lot: Mapped[int]
    vagrant_bonus_enemy_drop_item_lot: Mapped[int]
    vagrant_item_enemy_drop_item_lot: Mapped[int]
    can_be_stored: Mapped[bool]
    breaks_when_unequipped: Mapped[bool]
    disable_multiplayer_share: Mapped[bool]
    _pad1: Mapped[bytes]
    
    def __init__(self, id: int, source: EQUIP_PARAM_ACCESSORY_ST):
        self.id = id
        self.special_effect = source.SpecialEffect
        self.sfx_variation = source.SFXVariation
        self.weight = source.Weight
        self.behavior = source.Behavior
        self.basic_cost = source.BasicCost
        self.frampt_sell_value = source.FramptSellValue
        self.sort_index = source.SortIndex
        self.qwcid = source.QWCID
        self.equipment_model = source.EquipmentModel
        self.menu_icon = source.MenuIcon
        self.shop_level = source.ShopLevel
        self.achievement_contribution_id = source.AchievementContributionID
        self.achievement_unlock_id = source.AchievementUnlockID
        self.equipment_model_category = source.EquipmentModelCategory
        self.equipment_model_gender = source.EquipmentModelGender
        self.accessory_category = source.AccessoryCategory
        self.reference_type = source.ReferenceType
        self.special_effect_category = source.SpecialEffectCategory
        self._pad0 = source._Pad0
        self.vagrant_item_lot = source.VagrantItemLot
        self.vagrant_bonus_enemy_drop_item_lot = source.VagrantBonusEnemyDropItemLot
        self.vagrant_item_enemy_drop_item_lot = source.VagrantItemEnemyDropItemLot
        self.can_be_stored = source.CanBeStored
        self.breaks_when_unequipped = source.BreaksWhenUnequipped
        self.disable_multiplayer_share = source.DisableMultiplayerShare
        self._pad1 = source._Pad1