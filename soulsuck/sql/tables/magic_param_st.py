from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import MAGIC_PARAM_ST


class MagicParamST(Base):
    __tablename__ = "magic_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    confirmation_message: Mapped[int]
    limit_remove_special_effect: Mapped[int]
    sort_index: Mapped[int]
    reference_id: Mapped[int]
    mp_cost: Mapped[int]
    stamina_cost: Mapped[int]
    spell_icon: Mapped[int]
    behavior: Mapped[int]
    required_good: Mapped[int]
    replace_spell: Mapped[int]
    base_cast_count: Mapped[int]
    humanity_cost: Mapped[int]
    over_dexterity: Mapped[int]
    visual_effect_variation: Mapped[int]
    attunement_slots_used: Mapped[int]
    required_intelligence: Mapped[int]
    required_faith: Mapped[int]
    min_dexterity_for_bonus: Mapped[int]
    max_dexterity_for_bonus: Mapped[int]
    spell_category: Mapped[int]
    reference_type: Mapped[int]
    special_effect_category: Mapped[int]
    animation_type: Mapped[int]
    menu_activated: Mapped[int]
    has_special_effect_type: Mapped[int]
    replace_category: Mapped[int]
    limit_category: Mapped[int]
    useable_by_no_covenant: Mapped[bool]
    useable_by_way_of_white: Mapped[bool]
    useable_by_princess_guard: Mapped[bool]
    useable_by_warriors_of_sunlight: Mapped[bool]
    useable_by_darkwraith: Mapped[bool]
    useable_by_path_of_the_dragon: Mapped[bool]
    useable_by_gravelord_servant: Mapped[bool]
    useable_by_forest_hunter: Mapped[bool]
    useable_in_multiplayer: Mapped[bool]
    disabled_outside_multiplayer: Mapped[bool]
    is_weapon_buff: Mapped[bool]
    is_shield_buff: Mapped[bool]
    useable_by_humans: Mapped[bool]
    useable_by_hollows: Mapped[bool]
    useable_by_white_phantoms: Mapped[bool]
    useable_by_black_phantoms: Mapped[bool]
    disabled_offline: Mapped[bool]
    create_resonance_ring: Mapped[bool]
    _bit_pad0: Mapped[int]
    useable_by_darkmoon_blade: Mapped[bool]
    useable_by_chaos_servant: Mapped[bool]
    useable_by_covenant10: Mapped[bool]
    useable_by_covenant11: Mapped[bool]
    useable_by_covenant12: Mapped[bool]
    useable_by_covenant13: Mapped[bool]
    useable_by_covenant14: Mapped[bool]
    useable_by_covenant15: Mapped[bool]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: MAGIC_PARAM_ST):
        self.id = id
        self.confirmation_message = source.ConfirmationMessage
        self.limit_remove_special_effect = source.LimitRemoveSpecialEffect
        self.sort_index = source.SortIndex
        self.reference_id = source.ReferenceID
        self.mp_cost = source.MPCost
        self.stamina_cost = source.StaminaCost
        self.spell_icon = source.SpellIcon
        self.behavior = source.Behavior
        self.required_good = source.RequiredGood
        self.replace_spell = source.ReplaceSpell
        self.base_cast_count = source.BaseCastCount
        self.humanity_cost = source.HumanityCost
        self.over_dexterity = source.OverDexterity
        self.visual_effect_variation = source.VisualEffectVariation
        self.attunement_slots_used = source.AttunementSlotsUsed
        self.required_intelligence = source.RequiredIntelligence
        self.required_faith = source.RequiredFaith
        self.min_dexterity_for_bonus = source.MinDexterityForBonus
        self.max_dexterity_for_bonus = source.MaxDexterityForBonus
        self.spell_category = source.SpellCategory
        self.reference_type = source.ReferenceType
        self.special_effect_category = source.SpecialEffectCategory
        self.animation_type = source.AnimationType
        self.menu_activated = source.MenuActivated
        self.has_special_effect_type = source.HasSpecialEffectType
        self.replace_category = source.ReplaceCategory
        self.limit_category = source.LimitCategory
        self.useable_by_no_covenant = source.UseableByNoCovenant
        self.useable_by_way_of_white = source.UseableByWayOfWhite
        self.useable_by_princess_guard = source.UseableByPrincessGuard
        self.useable_by_warriors_of_sunlight = source.UseableByWarriorsOfSunlight
        self.useable_by_darkwraith = source.UseableByDarkwraith
        self.useable_by_path_of_the_dragon = source.UseableByPathOfTheDragon
        self.useable_by_gravelord_servant = source.UseableByGravelordServant
        self.useable_by_forest_hunter = source.UseableByForestHunter
        self.useable_in_multiplayer = source.UseableInMultiplayer
        self.disabled_outside_multiplayer = source.DisabledOutsideMultiplayer
        self.is_weapon_buff = source.IsWeaponBuff
        self.is_shield_buff = source.IsShieldBuff
        self.useable_by_humans = source.UseableByHumans
        self.useable_by_hollows = source.UseableByHollows
        self.useable_by_white_phantoms = source.UseableByWhitePhantoms
        self.useable_by_black_phantoms = source.UseableByBlackPhantoms
        self.disabled_offline = source.DisabledOffline
        self.create_resonance_ring = source.CreateResonanceRing
        self._bit_pad0 = source._BitPad0
        self.useable_by_darkmoon_blade = source.UseableByDarkmoonBlade
        self.useable_by_chaos_servant = source.UseableByChaosServant
        self.useable_by_covenant10 = source.UseableByCovenant10
        self.useable_by_covenant11 = source.UseableByCovenant11
        self.useable_by_covenant12 = source.UseableByCovenant12
        self.useable_by_covenant13 = source.UseableByCovenant13
        self.useable_by_covenant14 = source.UseableByCovenant14
        self.useable_by_covenant15 = source.UseableByCovenant15
        self._pad0 = source._Pad0