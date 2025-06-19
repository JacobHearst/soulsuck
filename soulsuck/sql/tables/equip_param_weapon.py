from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import EQUIP_PARAM_WEAPON_ST


class EquipParamWeaponST(Base):
    __tablename__ = "equip_param_weapon_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    behavior_variation_id: Mapped[int]
    sort_index: Mapped[int]
    ghost_weapon_replacement: Mapped[int]
    weight: Mapped[float]
    weight_ratio: Mapped[float]
    repair_cost: Mapped[int]
    basic_cost: Mapped[int]
    frampt_sell_value: Mapped[int]
    strength_scaling: Mapped[float]
    dexterity_scaling: Mapped[float]
    intelligence_scaling: Mapped[float]
    faith_scaling: Mapped[float]
    physical_guard_percentage: Mapped[float]
    magic_guard_percentage: Mapped[float]
    fire_guard_percentage: Mapped[float]
    lightning_guard_percentage: Mapped[float]
    special_effect_on_hit0: Mapped[int]
    special_effect_on_hit1: Mapped[int]
    special_effect_on_hit2: Mapped[int]
    equipped_special_effect0: Mapped[int]
    equipped_special_effect1: Mapped[int]
    equipped_special_effect2: Mapped[int]
    upgrade_material_id: Mapped[int]
    upgrade_origin0: Mapped[int]
    upgrade_origin1: Mapped[int]
    upgrade_origin2: Mapped[int]
    upgrade_origin3: Mapped[int]
    upgrade_origin4: Mapped[int]
    upgrade_origin5: Mapped[int]
    upgrade_origin6: Mapped[int]
    upgrade_origin7: Mapped[int]
    upgrade_origin8: Mapped[int]
    upgrade_origin9: Mapped[int]
    upgrade_origin10: Mapped[int]
    upgrade_origin11: Mapped[int]
    upgrade_origin12: Mapped[int]
    upgrade_origin13: Mapped[int]
    upgrade_origin14: Mapped[int]
    upgrade_origin15: Mapped[int]
    damage_against_demons_multiplier: Mapped[float]
    weak_to_divine_damage_multiplier: Mapped[float]
    god_damage_multiplier: Mapped[float]
    abyss_damage_multiplier: Mapped[float]
    vagrant_item_lot: Mapped[int]
    vagrant_bonus_enemy_drop_item_lot: Mapped[int]
    vagrant_item_enemy_drop_item_lot: Mapped[int]
    weapon_model: Mapped[int]
    weapon_icon: Mapped[int]
    initial_durability: Mapped[int]
    max_durability: Mapped[int]
    throw_escape_power: Mapped[int]
    max_parry_window_duration: Mapped[int]
    base_physical_damage: Mapped[int]
    base_magic_damage: Mapped[int]
    base_fire_damage: Mapped[int]
    base_lightning_damage: Mapped[int]
    base_stamina_damage: Mapped[int]
    base_poise_damage: Mapped[int]
    attack_poise_bonus: Mapped[int]
    effective_guard_angle: Mapped[int]
    guard_stamina_defense: Mapped[int]
    weapon_upgrade_id: Mapped[int]
    all_weapons_achievement_index: Mapped[int]
    max_upgrade_achievement_id: Mapped[int]
    throw_damage_change_percentage: Mapped[int]
    bow_range_change_percentage: Mapped[int]
    weapon_model_category: Mapped[int]
    weapon_model_gender: Mapped[int]
    weapon_category: Mapped[int]
    attack_animation_category: Mapped[int]
    guard_animation_category: Mapped[int]
    visual_sound_effects_on_hit: Mapped[int]
    visual_effects_on_block: Mapped[int]
    sound_effects_on_block: Mapped[int]
    scaling_formula_type: Mapped[int]
    element_attribute: Mapped[int]
    special_attack_category: Mapped[int]
    one_handed_animation_category: Mapped[int]
    two_handed_animation_category: Mapped[int]
    required_strength: Mapped[int]
    required_dexterity: Mapped[int]
    required_intelligence: Mapped[int]
    required_faith: Mapped[int]
    over_strength: Mapped[int]
    attack_base_parry: Mapped[int]
    defense_base_parry: Mapped[int]
    deflect_on_block: Mapped[int]
    deflect_on_attack: Mapped[int]
    ignore_guard_percentage: Mapped[int]
    guard_level: Mapped[int]
    slash_damage_reduction_when_guarding: Mapped[int]
    strike_damage_reduction_when_guarding: Mapped[int]
    thrust_damage_reduction_when_guarding: Mapped[int]
    poison_damage_reduction_when_guarding: Mapped[int]
    toxic_damage_reduction_when_guarding: Mapped[int]
    bleed_damage_reduction_when_guarding: Mapped[int]
    curse_damage_reduction_when_guarding: Mapped[int]
    durability_divergence_category: Mapped[int]
    right_hand_allowed: Mapped[bool]
    left_hand_allowed: Mapped[bool]
    both_hands_allowed: Mapped[bool]
    uses_equipped_arrows: Mapped[bool]
    uses_equipped_bolts: Mapped[bool]
    guard_enabled: Mapped[bool]
    parry_enabled: Mapped[bool]
    can_cast_sorceries: Mapped[bool]
    can_cast_pyromancy: Mapped[bool]
    can_cast_miracles: Mapped[bool]
    can_cast_covenant_magic: Mapped[bool]
    deals_neutral_damage: Mapped[bool]
    deals_strike_damage: Mapped[bool]
    deals_slash_damage: Mapped[bool]
    deals_thrust_damage: Mapped[bool]
    is_upgraded: Mapped[bool]
    is_affected_by_luck: Mapped[bool]
    is_custom: Mapped[bool]
    disable_base_change_reset: Mapped[bool]
    disable_repairs: Mapped[bool]
    is_dark_hand: Mapped[bool]
    simple_dlc_model_exists: Mapped[bool]
    is_lantern: Mapped[bool]
    can_hit_ghosts: Mapped[bool]
    base_change_category: Mapped[int]
    is_dragon_slayer: Mapped[bool]
    can_be_stored: Mapped[bool]
    disable_multiplayer_share: Mapped[bool]
    _pad0: Mapped[bytes]
    old_sort_index: Mapped[int]
    _pad1: Mapped[bytes]
    
    def __init__(self, id: int, source: EQUIP_PARAM_WEAPON_ST):
        self.id = id
        self.behavior_variation_id = source.BehaviorVariationID
        self.sort_index = source.SortIndex
        self.ghost_weapon_replacement = source.GhostWeaponReplacement
        self.weight = source.Weight
        self.weight_ratio = source.WeightRatio
        self.repair_cost = source.RepairCost
        self.basic_cost = source.BasicCost
        self.frampt_sell_value = source.FramptSellValue
        self.strength_scaling = source.StrengthScaling
        self.dexterity_scaling = source.DexterityScaling
        self.intelligence_scaling = source.IntelligenceScaling
        self.faith_scaling = source.FaithScaling
        self.physical_guard_percentage = source.PhysicalGuardPercentage
        self.magic_guard_percentage = source.MagicGuardPercentage
        self.fire_guard_percentage = source.FireGuardPercentage
        self.lightning_guard_percentage = source.LightningGuardPercentage
        self.special_effect_on_hit0 = source.SpecialEffectOnHit0
        self.special_effect_on_hit1 = source.SpecialEffectOnHit1
        self.special_effect_on_hit2 = source.SpecialEffectOnHit2
        self.equipped_special_effect0 = source.EquippedSpecialEffect0
        self.equipped_special_effect1 = source.EquippedSpecialEffect1
        self.equipped_special_effect2 = source.EquippedSpecialEffect2
        self.upgrade_material_id = source.UpgradeMaterialID
        self.upgrade_origin0 = source.UpgradeOrigin0
        self.upgrade_origin1 = source.UpgradeOrigin1
        self.upgrade_origin2 = source.UpgradeOrigin2
        self.upgrade_origin3 = source.UpgradeOrigin3
        self.upgrade_origin4 = source.UpgradeOrigin4
        self.upgrade_origin5 = source.UpgradeOrigin5
        self.upgrade_origin6 = source.UpgradeOrigin6
        self.upgrade_origin7 = source.UpgradeOrigin7
        self.upgrade_origin8 = source.UpgradeOrigin8
        self.upgrade_origin9 = source.UpgradeOrigin9
        self.upgrade_origin10 = source.UpgradeOrigin10
        self.upgrade_origin11 = source.UpgradeOrigin11
        self.upgrade_origin12 = source.UpgradeOrigin12
        self.upgrade_origin13 = source.UpgradeOrigin13
        self.upgrade_origin14 = source.UpgradeOrigin14
        self.upgrade_origin15 = source.UpgradeOrigin15
        self.damage_against_demons_multiplier = source.DamageAgainstDemonsMultiplier
        self.weak_to_divine_damage_multiplier = source.WeakToDivineDamageMultiplier
        self.god_damage_multiplier = source.GodDamageMultiplier
        self.abyss_damage_multiplier = source.AbyssDamageMultiplier
        self.vagrant_item_lot = source.VagrantItemLot
        self.vagrant_bonus_enemy_drop_item_lot = source.VagrantBonusEnemyDropItemLot
        self.vagrant_item_enemy_drop_item_lot = source.VagrantItemEnemyDropItemLot
        self.weapon_model = source.WeaponModel
        self.weapon_icon = source.WeaponIcon
        self.initial_durability = source.InitialDurability
        self.max_durability = source.MaxDurability
        self.throw_escape_power = source.ThrowEscapePower
        self.max_parry_window_duration = source.MaxParryWindowDuration
        self.base_physical_damage = source.BasePhysicalDamage
        self.base_magic_damage = source.BaseMagicDamage
        self.base_fire_damage = source.BaseFireDamage
        self.base_lightning_damage = source.BaseLightningDamage
        self.base_stamina_damage = source.BaseStaminaDamage
        self.base_poise_damage = source.BasePoiseDamage
        self.attack_poise_bonus = source.AttackPoiseBonus
        self.effective_guard_angle = source.EffectiveGuardAngle
        self.guard_stamina_defense = source.GuardStaminaDefense
        self.weapon_upgrade_id = source.WeaponUpgradeID
        self.all_weapons_achievement_index = source.AllWeaponsAchievementIndex
        self.max_upgrade_achievement_id = source.MaxUpgradeAchievementID
        self.throw_damage_change_percentage = source.ThrowDamageChangePercentage
        self.bow_range_change_percentage = source.BowRangeChangePercentage
        self.weapon_model_category = source.WeaponModelCategory
        self.weapon_model_gender = source.WeaponModelGender
        self.weapon_category = source.WeaponCategory
        self.attack_animation_category = source.AttackAnimationCategory
        self.guard_animation_category = source.GuardAnimationCategory
        self.visual_sound_effects_on_hit = source.VisualSoundEffectsOnHit
        self.visual_effects_on_block = source.VisualEffectsOnBlock
        self.sound_effects_on_block = source.SoundEffectsOnBlock
        self.scaling_formula_type = source.ScalingFormulaType
        self.element_attribute = source.ElementAttribute
        self.special_attack_category = source.SpecialAttackCategory
        self.one_handed_animation_category = source.OneHandedAnimationCategory
        self.two_handed_animation_category = source.TwoHandedAnimationCategory
        self.required_strength = source.RequiredStrength
        self.required_dexterity = source.RequiredDexterity
        self.required_intelligence = source.RequiredIntelligence
        self.required_faith = source.RequiredFaith
        self.over_strength = source.OverStrength
        self.attack_base_parry = source.AttackBaseParry
        self.defense_base_parry = source.DefenseBaseParry
        self.deflect_on_block = source.DeflectOnBlock
        self.deflect_on_attack = source.DeflectOnAttack
        self.ignore_guard_percentage = source.IgnoreGuardPercentage
        self.guard_level = source.GuardLevel
        self.slash_damage_reduction_when_guarding = source.SlashDamageReductionWhenGuarding
        self.strike_damage_reduction_when_guarding = source.StrikeDamageReductionWhenGuarding
        self.thrust_damage_reduction_when_guarding = source.ThrustDamageReductionWhenGuarding
        self.poison_damage_reduction_when_guarding = source.PoisonDamageReductionWhenGuarding
        self.toxic_damage_reduction_when_guarding = source.ToxicDamageReductionWhenGuarding
        self.bleed_damage_reduction_when_guarding = source.BleedDamageReductionWhenGuarding
        self.curse_damage_reduction_when_guarding = source.CurseDamageReductionWhenGuarding
        self.durability_divergence_category = source.DurabilityDivergenceCategory
        self.right_hand_allowed = source.RightHandAllowed
        self.left_hand_allowed = source.LeftHandAllowed
        self.both_hands_allowed = source.BothHandsAllowed
        self.uses_equipped_arrows = source.UsesEquippedArrows
        self.uses_equipped_bolts = source.UsesEquippedBolts
        self.guard_enabled = source.GuardEnabled
        self.parry_enabled = source.ParryEnabled
        self.can_cast_sorceries = source.CanCastSorceries
        self.can_cast_pyromancy = source.CanCastPyromancy
        self.can_cast_miracles = source.CanCastMiracles
        self.can_cast_covenant_magic = source.CanCastCovenantMagic
        self.deals_neutral_damage = source.DealsNeutralDamage
        self.deals_strike_damage = source.DealsStrikeDamage
        self.deals_slash_damage = source.DealsSlashDamage
        self.deals_thrust_damage = source.DealsThrustDamage
        self.is_upgraded = source.IsUpgraded
        self.is_affected_by_luck = source.IsAffectedByLuck
        self.is_custom = source.IsCustom
        self.disable_base_change_reset = source.DisableBaseChangeReset
        self.disable_repairs = source.DisableRepairs
        self.is_dark_hand = source.IsDarkHand
        self.simple_dlc_model_exists = source.SimpleDLCModelExists
        self.is_lantern = source.IsLantern
        self.can_hit_ghosts = source.CanHitGhosts
        self.base_change_category = source.BaseChangeCategory
        self.is_dragon_slayer = source.IsDragonSlayer
        self.can_be_stored = source.CanBeStored
        self.disable_multiplayer_share = source.DisableMultiplayerShare
        self._pad0 = source._Pad0
        self.old_sort_index = source.OldSortIndex
        self._pad1 = source._Pad1