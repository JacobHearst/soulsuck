from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import EQUIP_PARAM_GOODS_ST


class EquipParamGoodsST(Base):
    __tablename__ = "equip_param_goods_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    reference_id: Mapped[int]
    animation_variation_id: Mapped[int]
    weight: Mapped[float]
    basic_cost: Mapped[int]
    frampt_sell_value: Mapped[int]
    behavior: Mapped[int]
    good_to_replace: Mapped[int]
    sort_index: Mapped[int]
    qwcid: Mapped[int]
    confirmation_message: Mapped[int]
    spell: Mapped[int]
    good_icon: Mapped[int]
    model_id: Mapped[int]
    shop_level: Mapped[int]
    collection_achievement_id: Mapped[int]
    achievement_id: Mapped[int]
    max_hold_quantity: Mapped[int]
    humanity_cost: Mapped[int]
    over_dexterity: Mapped[int]
    good_type: Mapped[int]
    reference_type: Mapped[int]
    special_effect_category: Mapped[int]
    good_category: Mapped[int]
    use_animation: Mapped[int]
    menu_activated: Mapped[int]
    limit_category: Mapped[int]
    replace_category: Mapped[int]
    useable_by_no_covenant: Mapped[bool]
    useable_by_way_of_white: Mapped[bool]
    useable_by_princess_guard: Mapped[bool]
    useable_by_warriors_of_sunlight: Mapped[bool]
    useable_by_darkwraith: Mapped[bool]
    useable_by_path_of_the_dragon: Mapped[bool]
    useable_by_gravelord_servant: Mapped[bool]
    useable_by_forest_hunter: Mapped[bool]
    useable_by_darkmoon_blade: Mapped[bool]
    useable_by_chaos_servant: Mapped[bool]
    useable_by_covenant10: Mapped[bool]
    useable_by_covenant11: Mapped[bool]
    useable_by_covenant12: Mapped[bool]
    useable_by_covenant13: Mapped[bool]
    useable_by_covenant14: Mapped[bool]
    useable_by_covenant15: Mapped[bool]
    useable_by_humans: Mapped[bool]
    useable_by_hollows: Mapped[bool]
    useable_by_white_phantoms: Mapped[bool]
    useable_by_black_phantoms: Mapped[bool]
    useable_in_multiplayer: Mapped[bool]
    disabled_offline: Mapped[bool]
    can_be_equipped: Mapped[bool]
    consumed_on_use: Mapped[bool]
    automatically_equipped: Mapped[bool]
    is_stationary: Mapped[bool]
    is_unique: Mapped[bool]
    can_be_dropped: Mapped[bool]
    can_be_stored: Mapped[bool]
    is_disable_hand: Mapped[bool]
    is_travel_item: Mapped[bool]
    is_empty_estus_flask: Mapped[bool]
    is_non_empty_estus_flask: Mapped[bool]
    is_upgrade_material: Mapped[bool]
    is_fix_item: Mapped[bool]
    disable_multiplayer_share: Mapped[bool]
    disabled_in_arena: Mapped[bool]
    disabled_outside_arena: Mapped[bool]
    _pad0: Mapped[bytes]
    vagrant_item_lot: Mapped[int]
    vagrant_bonus_enemy_drop_item_lot: Mapped[int]
    vagrant_item_enemy_drop_item_lot: Mapped[int]
    
    def __init__(self, id: int, source: EQUIP_PARAM_GOODS_ST):
        self.id = id
        self.reference_id = source.ReferenceID
        self.animation_variation_id = source.AnimationVariationID
        self.weight = source.Weight
        self.basic_cost = source.BasicCost
        self.frampt_sell_value = source.FramptSellValue
        self.behavior = source.Behavior
        self.good_to_replace = source.GoodToReplace
        self.sort_index = source.SortIndex
        self.qwcid = source.QWCID
        self.confirmation_message = source.ConfirmationMessage
        self.spell = source.Spell
        self.good_icon = source.GoodIcon
        self.model_id = source.ModelID
        self.shop_level = source.ShopLevel
        self.collection_achievement_id = source.CollectionAchievementID
        self.achievement_id = source.AchievementID
        self.max_hold_quantity = source.MaxHoldQuantity
        self.humanity_cost = source.HumanityCost
        self.over_dexterity = source.OverDexterity
        self.good_type = source.GoodType
        self.reference_type = source.ReferenceType
        self.special_effect_category = source.SpecialEffectCategory
        self.good_category = source.GoodCategory
        self.use_animation = source.UseAnimation
        self.menu_activated = source.MenuActivated
        self.limit_category = source.LimitCategory
        self.replace_category = source.ReplaceCategory
        self.useable_by_no_covenant = source.UseableByNoCovenant
        self.useable_by_way_of_white = source.UseableByWayOfWhite
        self.useable_by_princess_guard = source.UseableByPrincessGuard
        self.useable_by_warriors_of_sunlight = source.UseableByWarriorsOfSunlight
        self.useable_by_darkwraith = source.UseableByDarkwraith
        self.useable_by_path_of_the_dragon = source.UseableByPathOfTheDragon
        self.useable_by_gravelord_servant = source.UseableByGravelordServant
        self.useable_by_forest_hunter = source.UseableByForestHunter
        self.useable_by_darkmoon_blade = source.UseableByDarkmoonBlade
        self.useable_by_chaos_servant = source.UseableByChaosServant
        self.useable_by_covenant10 = source.UseableByCovenant10
        self.useable_by_covenant11 = source.UseableByCovenant11
        self.useable_by_covenant12 = source.UseableByCovenant12
        self.useable_by_covenant13 = source.UseableByCovenant13
        self.useable_by_covenant14 = source.UseableByCovenant14
        self.useable_by_covenant15 = source.UseableByCovenant15
        self.useable_by_humans = source.UseableByHumans
        self.useable_by_hollows = source.UseableByHollows
        self.useable_by_white_phantoms = source.UseableByWhitePhantoms
        self.useable_by_black_phantoms = source.UseableByBlackPhantoms
        self.useable_in_multiplayer = source.UseableInMultiplayer
        self.disabled_offline = source.DisabledOffline
        self.can_be_equipped = source.CanBeEquipped
        self.consumed_on_use = source.ConsumedOnUse
        self.automatically_equipped = source.AutomaticallyEquipped
        self.is_stationary = source.IsStationary
        self.is_unique = source.IsUnique
        self.can_be_dropped = source.CanBeDropped
        self.can_be_stored = source.CanBeStored
        self.is_disable_hand = source.IsDisableHand
        self.is_travel_item = source.IsTravelItem
        self.is_empty_estus_flask = source.IsEmptyEstusFlask
        self.is_non_empty_estus_flask = source.IsNonEmptyEstusFlask
        self.is_upgrade_material = source.IsUpgradeMaterial
        self.is_fix_item = source.IsFixItem
        self.disable_multiplayer_share = source.DisableMultiplayerShare
        self.disabled_in_arena = source.DisabledInArena
        self.disabled_outside_arena = source.DisabledOutsideArena
        self._pad0 = source._Pad0
        self.vagrant_item_lot = source.VagrantItemLot
        self.vagrant_bonus_enemy_drop_item_lot = source.VagrantBonusEnemyDropItemLot
        self.vagrant_item_enemy_drop_item_lot = source.VagrantItemEnemyDropItemLot