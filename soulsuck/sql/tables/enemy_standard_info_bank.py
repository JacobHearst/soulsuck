from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import ENEMY_STANDARD_INFO_BANK


class EnemyStandardInfoBank(Base):
    __tablename__ = "enemy_standard_info_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    enemy_behavior_id: Mapped[int]
    hp: Mapped[int]
    attack_power: Mapped[int]
    chr_type: Mapped[int]
    hit_height: Mapped[float]
    hit_radius: Mapped[float]
    weight: Mapped[float]
    dynamic_friction: Mapped[float]
    static_friction: Mapped[float]
    upper_def_state: Mapped[int]
    action_def_state: Mapped[int]
    rot_y_per_second: Mapped[float]
    rot_y_per_second_old: Mapped[int]
    enable_side_step: Mapped[int]
    use_ragdoll_hit: Mapped[int]
    stamina: Mapped[int]
    stamina_recover: Mapped[int]
    stamina_consumption: Mapped[int]
    deffenct_phys: Mapped[int]
    
    def __init__(self, id: int, param: ENEMY_STANDARD_INFO_BANK):
        self.id = id
        self.enemy_behavior_id = param.EnemyBehaviorID
        self.hp = param.HP
        self.attack_power = param.AttackPower
        self.chr_type = param.ChrType
        self.hit_height = param.HitHeight
        self.hit_radius = param.HitRadius
        self.weight = param.Weight
        self.dynamic_friction = param.DynamicFriction
        self.static_friction = param.StaticFriction
        self.upper_def_state = param.UpperDefState
        self.action_def_state = param.ActionDefState
        self.rot_y_per_second = param.RotYperSecond
        self.rot_y_per_second_old = param.RotYperSecondold
        self.enable_side_step = param.EnableSideStep
        self.use_ragdoll_hit = param.UseRagdollHit
        self.stamina = param.Stamina
        self.stamina_recover = param.StaminaRecover
        self.stamina_consumption = param.StaminaConsumption
        self.deffenct_phys = param.DeffenctPhys
