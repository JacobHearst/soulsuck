from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import ATK_PARAM_ST

class AtkParamST(Base):
    __tablename__ = "atk_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    hitbox0_radius: Mapped[float]
    hitbox1_radius: Mapped[float]
    hitbox2_radius: Mapped[float]
    hitbox3_radius: Mapped[float]
    knockback_distance: Mapped[float]
    hit_stop_time: Mapped[float]
    special_effect_on_hit0: Mapped[int]
    special_effect_on_hit1: Mapped[int]
    special_effect_on_hit2: Mapped[int]
    special_effect_on_hit3: Mapped[int]
    special_effect_on_hit4: Mapped[int]
    hitbox0_start_model_point: Mapped[int]
    hitbox1_start_model_point: Mapped[int]
    hitbox2_start_model_point: Mapped[int]
    hitbox3_start_model_point: Mapped[int]
    hitbox0_end_model_point: Mapped[int]
    hitbox1_end_model_point: Mapped[int]
    hitbox2_end_model_point: Mapped[int]
    hitbox3_end_model_point: Mapped[int]
    blow_off_correction: Mapped[int]
    physical_attack_power_percentage: Mapped[int]
    magic_attack_power_percentage: Mapped[int]
    fire_attack_power_percentage: Mapped[int]
    lightning_attack_power_percentage: Mapped[int]
    stamina_attack_power_percentage: Mapped[int]
    guard_attack_percentage: Mapped[int]
    guard_break_percentage: Mapped[int]
    attack_during_throw_percentage: Mapped[int]
    poise_attack_percentage: Mapped[int]
    physical_attack_power: Mapped[int]
    magic_attack_power: Mapped[int]
    fire_attack_power: Mapped[int]
    lightning_attack_power: Mapped[int]
    stamina_attack_power: Mapped[int]
    guard_attack_power: Mapped[int]
    guard_break_power: Mapped[int]
    poise_attack_power: Mapped[int]
    attack_power_during_throws: Mapped[int]
    object_damage: Mapped[int]
    guard_stamina_percentage: Mapped[int]
    guard_percentage: Mapped[int]
    throw_id: Mapped[int]
    hitbox0_hit_type: Mapped[int]
    hitbox1_hit_type: Mapped[int]
    hitbox2_hit_type: Mapped[int]
    hitbox3_hit_type: Mapped[int]
    hitbox0_priority: Mapped[int]
    hitbox1_priority: Mapped[int]
    hitbox2_priority: Mapped[int]
    hitbox3_priority: Mapped[int]
    impact_level: Mapped[int]
    map_hit_type: Mapped[int]
    ignore_guard_percentage: Mapped[int]
    attack_attribute: Mapped[int]
    element_attribute: Mapped[int]
    visual_sound_effects_on_attack: Mapped[int]
    visual_sound_effects_on_hit: Mapped[int]
    attack_size: Mapped[int]
    sound_effects_while_blocking: Mapped[int]
    visual_effects_while_blocking: Mapped[int]
    model_point_source: Mapped[int]
    throw_flag: Mapped[int]
    ignore_guard: Mapped[bool]
    no_stamina_damage: Mapped[bool]
    no_special_effects: Mapped[bool]
    no_miss_notification_for_ai: Mapped[bool]
    repeat_hit_sound_effects: Mapped[bool]
    is_physical_projectile: Mapped[bool]
    is_attack_by_ghost: Mapped[bool]
    ignore_invincibility_frames: Mapped[bool]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: ATK_PARAM_ST):
        self.id = id
        self.hitbox0_radius = source.Hitbox0Radius
        self.hitbox1_radius = source.Hitbox1Radius
        self.hitbox2_radius = source.Hitbox2Radius
        self.hitbox3_radius = source.Hitbox3Radius
        self.knockback_distance = source.KnockbackDistance
        self.hit_stop_time = source.HitStopTime
        self.special_effect_on_hit0 = source.SpecialEffectOnHit0
        self.special_effect_on_hit1 = source.SpecialEffectOnHit1
        self.special_effect_on_hit2 = source.SpecialEffectOnHit2
        self.special_effect_on_hit3 = source.SpecialEffectOnHit3
        self.special_effect_on_hit4 = source.SpecialEffectOnHit4
        self.hitbox0_start_model_point = source.Hitbox0StartModelPoint
        self.hitbox1_start_model_point = source.Hitbox1StartModelPoint
        self.hitbox2_start_model_point = source.Hitbox2StartModelPoint
        self.hitbox3_start_model_point = source.Hitbox3StartModelPoint
        self.hitbox0_end_model_point = source.Hitbox0EndModelPoint
        self.hitbox1_end_model_point = source.Hitbox1EndModelPoint
        self.hitbox2_end_model_point = source.Hitbox2EndModelPoint
        self.hitbox3_end_model_point = source.Hitbox3EndModelPoint
        self.blow_off_correction = source.BlowOffCorrection
        self.physical_attack_power_percentage = source.PhysicalAttackPowerPercentage
        self.magic_attack_power_percentage = source.MagicAttackPowerPercentage
        self.fire_attack_power_percentage = source.FireAttackPowerPercentage
        self.lightning_attack_power_percentage = source.LightningAttackPowerPercentage
        self.stamina_attack_power_percentage = source.StaminaAttackPowerPercentage
        self.guard_attack_percentage = source.GuardAttackPercentage
        self.guard_break_percentage = source.GuardBreakPercentage
        self.attack_during_throw_percentage = source.AttackDuringThrowPercentage
        self.poise_attack_percentage = source.PoiseAttackPercentage
        self.physical_attack_power = source.PhysicalAttackPower
        self.magic_attack_power = source.MagicAttackPower
        self.fire_attack_power = source.FireAttackPower
        self.lightning_attack_power = source.LightningAttackPower
        self.stamina_attack_power = source.StaminaAttackPower
        self.guard_attack_power = source.GuardAttackPower
        self.guard_break_power = source.GuardBreakPower
        self.poise_attack_power = source.PoiseAttackPower
        self.attack_power_during_throws = source.AttackPowerDuringThrows
        self.object_damage = source.ObjectDamage
        self.guard_stamina_percentage = source.GuardStaminaPercentage
        self.guard_percentage = source.GuardPercentage
        self.throw_id = source.ThrowID
        self.hitbox0_hit_type = source.Hitbox0HitType
        self.hitbox1_hit_type = source.Hitbox1HitType
        self.hitbox2_hit_type = source.Hitbox2HitType
        self.hitbox3_hit_type = source.Hitbox3HitType
        self.hitbox0_priority = source.Hitbox0Priority
        self.hitbox1_priority = source.Hitbox1Priority
        self.hitbox2_priority = source.Hitbox2Priority
        self.hitbox3_priority = source.Hitbox3Priority
        self.impact_level = source.ImpactLevel
        self.map_hit_type = source.MapHitType
        self.ignore_guard_percentage = source.IgnoreGuardPercentage
        self.attack_attribute = source.AttackAttribute
        self.element_attribute = source.ElementAttribute
        self.visual_sound_effects_on_attack = source.VisualSoundEffectsOnAttack
        self.visual_sound_effects_on_hit = source.VisualSoundEffectsOnHit
        self.attack_size = source.AttackSize
        self.sound_effects_while_blocking = source.SoundEffectsWhileBlocking
        self.visual_effects_while_blocking = source.VisualEffectsWhileBlocking
        self.model_point_source = source.ModelPointSource
        self.throw_flag = source.ThrowFlag
        self.ignore_guard = source.IgnoreGuard
        self.no_stamina_damage = source.NoStaminaDamage
        self.no_special_effects = source.NoSpecialEffects
        self.no_miss_notification_for_ai = source.NoMissNotificationForAI
        self.repeat_hit_sound_effects = source.RepeatHitSoundEffects
        self.is_physical_projectile = source.IsPhysicalProjectile
        self.is_attack_by_ghost = source.IsAttackByGhost
        self.ignore_invincibility_frames = source.IgnoreInvincibilityFrames
        self._pad0 = source._Pad0


# class AtkParam_Npc(AtkParamST):
#     pass

# class AtkParam_Pc(AtkParamST):
#     pass