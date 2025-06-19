from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import REINFORCE_PARAM_WEAPON_ST


class ReinforceParamWeaponST(Base):
    __tablename__ = "reinforce_param_weapon_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    physical_damage_multiplier: Mapped[float]
    magic_damage_multiplier: Mapped[float]
    fire_damage_multiplier: Mapped[float]
    lightning_damage_multiplier: Mapped[float]
    stamina_damage_multiplier: Mapped[float]
    poise_damage_multiplier: Mapped[float]
    poise_defense_multiplier: Mapped[float]
    strength_scaling_multiplier: Mapped[float]
    dexterity_scaling_multiplier: Mapped[float]
    intelligence_scaling_multiplier: Mapped[float]
    faith_scaling_multiplier: Mapped[float]
    physical_guard_reduction_multiplier: Mapped[float]
    magic_guard_reduction_multiplier: Mapped[float]
    fire_guard_reduction_multiplier: Mapped[float]
    lightning_guard_reduction_multiplier: Mapped[float]
    poison_guard_resistance_multiplier: Mapped[float]
    toxic_guard_resistance_multiplier: Mapped[float]
    bleed_guard_resistance_multiplier: Mapped[float]
    curse_guard_resistance_multiplier: Mapped[float]
    stamina_guard_reduction_multiplier: Mapped[float]
    special_effect_on_hit0: Mapped[int]
    special_effect_on_hit1: Mapped[int]
    special_effect_on_hit2: Mapped[int]
    equipped_special_effect0: Mapped[int]
    equipped_special_effect1: Mapped[int]
    equipped_special_effect2: Mapped[int]
    upgrade_material_offset: Mapped[int]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: REINFORCE_PARAM_WEAPON_ST):
        self.id = id
        self.physical_damage_multiplier = source.PhysicalDamageMultiplier
        self.magic_damage_multiplier = source.MagicDamageMultiplier
        self.fire_damage_multiplier = source.FireDamageMultiplier
        self.lightning_damage_multiplier = source.LightningDamageMultiplier
        self.stamina_damage_multiplier = source.StaminaDamageMultiplier
        self.poise_damage_multiplier = source.PoiseDamageMultiplier
        self.poise_defense_multiplier = source.PoiseDefenseMultiplier
        self.strength_scaling_multiplier = source.StrengthScalingMultiplier
        self.dexterity_scaling_multiplier = source.DexterityScalingMultiplier
        self.intelligence_scaling_multiplier = source.IntelligenceScalingMultiplier
        self.faith_scaling_multiplier = source.FaithScalingMultiplier
        self.physical_guard_reduction_multiplier = source.PhysicalGuardReductionMultiplier
        self.magic_guard_reduction_multiplier = source.MagicGuardReductionMultiplier
        self.fire_guard_reduction_multiplier = source.FireGuardReductionMultiplier
        self.lightning_guard_reduction_multiplier = source.LightningGuardReductionMultiplier
        self.poison_guard_resistance_multiplier = source.PoisonGuardResistanceMultiplier
        self.toxic_guard_resistance_multiplier = source.ToxicGuardResistanceMultiplier
        self.bleed_guard_resistance_multiplier = source.BleedGuardResistanceMultiplier
        self.curse_guard_resistance_multiplier = source.CurseGuardResistanceMultiplier
        self.stamina_guard_reduction_multiplier = source.StaminaGuardReductionMultiplier
        self.special_effect_on_hit0 = source.SpecialEffectOnHit0
        self.special_effect_on_hit1 = source.SpecialEffectOnHit1
        self.special_effect_on_hit2 = source.SpecialEffectOnHit2
        self.equipped_special_effect0 = source.EquippedSpecialEffect0
        self.equipped_special_effect1 = source.EquippedSpecialEffect1
        self.equipped_special_effect2 = source.EquippedSpecialEffect2
        self.upgrade_material_offset = source.UpgradeMaterialOffset
        self._pad0 = source._Pad0