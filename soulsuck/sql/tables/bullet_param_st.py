from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import BULLET_PARAM_ST


class BulletParamST(Base):
    __tablename__ = "bullet_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    bullet_attack: Mapped[int]
    projectile_vfx: Mapped[int]
    impact_vfx: Mapped[int]
    flick_vfx: Mapped[int]
    life_time: Mapped[float]
    attenuation_distance: Mapped[float]
    launch_interval: Mapped[float]
    gravity_before_attenuation: Mapped[float]
    gravity_after_attenuation: Mapped[float]
    closest_homing_distance: Mapped[float]
    initial_speed: Mapped[float]
    acceleration_before_attenuation: Mapped[float]
    acceleration_after_attenuation: Mapped[float]
    max_speed: Mapped[float]
    min_speed: Mapped[float]
    acceleration_time: Mapped[float]
    homing_start_distance: Mapped[float]
    initial_hit_radius: Mapped[float]
    final_hit_radius: Mapped[float]
    radius_increase_time: Mapped[float]
    exp_delay: Mapped[float]
    homing_offset_range: Mapped[float]
    hitbox_life_time: Mapped[float]
    external_force: Mapped[float]
    owner_special_effect: Mapped[int]
    bullet_ai: Mapped[int]
    bullet_on_hit: Mapped[int]
    hit_special_effect0: Mapped[int]
    hit_special_effect1: Mapped[int]
    hit_special_effect2: Mapped[int]
    hit_special_effect3: Mapped[int]
    hit_special_effect4: Mapped[int]
    bullet_count: Mapped[int]
    homing_angle_per_second: Mapped[int]
    azimuth_angle_start: Mapped[int]
    azimuth_angle_interval: Mapped[int]
    elevation_angle_interval: Mapped[int]
    physical_damage_damp: Mapped[int]
    magic_damage_damp: Mapped[int]
    fire_damage_damp: Mapped[int]
    lightning_damage_damp: Mapped[int]
    stamina_damp: Mapped[int]
    knockback_damp: Mapped[int]
    first_bullet_elevation_angle: Mapped[int]
    lock_shoot_limit_angle: Mapped[int]
    pierces_targets: Mapped[int]
    previous_direction_ratio: Mapped[int]
    attack_attribute: Mapped[int]
    element_attribute: Mapped[int]
    material_attack_type: Mapped[int]
    effects_on_hit: Mapped[int]
    material_size: Mapped[int]
    launch_condition_type: Mapped[int]
    follow_type: Mapped[int]
    origin_type: Mapped[int]
    remain_attached_to_target: Mapped[bool]
    is_endless_hit: Mapped[bool]
    is_map_piercing: Mapped[bool]
    hits_both_teams: Mapped[bool]
    shared_hit_check: Mapped[bool]
    uses_multiple_model_points: Mapped[bool]
    attach_effect_type: Mapped[int]
    can_be_deflected_by_magic: Mapped[bool]
    ignore_vfx_on_water_hit: Mapped[bool]
    ignore_state_transition_on_water_hit: Mapped[bool]
    can_be_deflected_by_silver_pendant: Mapped[bool]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: BULLET_PARAM_ST):
        self.id = id
        self.bullet_attack = source.BulletAttack
        self.projectile_vfx = source.ProjectileVFX
        self.impact_vfx = source.ImpactVFX
        self.flick_vfx = source.FlickVFX
        self.life_time = source.LifeTime
        self.attenuation_distance = source.AttenuationDistance
        self.launch_interval = source.LaunchInterval
        self.gravity_before_attenuation = source.GravityBeforeAttenuation
        self.gravity_after_attenuation = source.GravityAfterAttenuation
        self.closest_homing_distance = source.ClosestHomingDistance
        self.initial_speed = source.InitialSpeed
        self.acceleration_before_attenuation = source.AccelerationBeforeAttenuation
        self.acceleration_after_attenuation = source.AccelerationAfterAttenuation
        self.max_speed = source.MaxSpeed
        self.min_speed = source.MinSpeed
        self.acceleration_time = source.AccelerationTime
        self.homing_start_distance = source.HomingStartDistance
        self.initial_hit_radius = source.InitialHitRadius
        self.final_hit_radius = source.FinalHitRadius
        self.radius_increase_time = source.RadiusIncreaseTime
        self.exp_delay = source.ExpDelay
        self.homing_offset_range = source.HomingOffsetRange
        self.hitbox_life_time = source.HitboxLifeTime
        self.external_force = source.ExternalForce
        self.owner_special_effect = source.OwnerSpecialEffect
        self.bullet_ai = source.BulletAI
        self.bullet_on_hit = source.BulletOnHit
        self.hit_special_effect0 = source.HitSpecialEffect0
        self.hit_special_effect1 = source.HitSpecialEffect1
        self.hit_special_effect2 = source.HitSpecialEffect2
        self.hit_special_effect3 = source.HitSpecialEffect3
        self.hit_special_effect4 = source.HitSpecialEffect4
        self.bullet_count = source.BulletCount
        self.homing_angle_per_second = source.HomingAnglePerSecond
        self.azimuth_angle_start = source.AzimuthAngleStart
        self.azimuth_angle_interval = source.AzimuthAngleInterval
        self.elevation_angle_interval = source.ElevationAngleInterval
        self.physical_damage_damp = source.PhysicalDamageDamp
        self.magic_damage_damp = source.MagicDamageDamp
        self.fire_damage_damp = source.FireDamageDamp
        self.lightning_damage_damp = source.LightningDamageDamp
        self.stamina_damp = source.StaminaDamp
        self.knockback_damp = source.KnockbackDamp
        self.first_bullet_elevation_angle = source.FirstBulletElevationAngle
        self.lock_shoot_limit_angle = source.LockShootLimitAngle
        self.pierces_targets = source.PiercesTargets
        self.previous_direction_ratio = source.PreviousDirectionRatio
        self.attack_attribute = source.AttackAttribute
        self.element_attribute = source.ElementAttribute
        self.material_attack_type = source.MaterialAttackType
        self.effects_on_hit = source.EffectsOnHit
        self.material_size = source.MaterialSize
        self.launch_condition_type = source.LaunchConditionType
        self.follow_type = source.FollowType
        self.origin_type = source.OriginType
        self.remain_attached_to_target = source.RemainAttachedToTarget
        self.is_endless_hit = source.IsEndlessHit
        self.is_map_piercing = source.IsMapPiercing
        self.hits_both_teams = source.HitsBothTeams
        self.shared_hit_check = source.SharedHitCheck
        self.uses_multiple_model_points = source.UsesMultipleModelPoints
        self.attach_effect_type = source.AttachEffectType
        self.can_be_deflected_by_magic = source.CanBeDeflectedByMagic
        self.ignore_vfx_on_water_hit = source.IgnoreVFXOnWaterHit
        self.ignore_state_transition_on_water_hit = source.IgnoreStateTransitionOnWaterHit
        self.can_be_deflected_by_silver_pendant = source.CanBeDeflectedBySilverPendant
        self._pad0 = source._Pad0