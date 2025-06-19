from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import KNOCKBACK_PARAM_ST


class KnockbackParamST(Base):
    __tablename__ = "knockback_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    damage_min_cont_time: Mapped[float]
    damage_s_cont_time: Mapped[float]
    damage_m_cont_time: Mapped[float]
    damage_l_cont_time: Mapped[float]
    damage_blow_s_cont_time: Mapped[float]
    damage_blow_m_cont_time: Mapped[float]
    damage_strike_cont_time: Mapped[float]
    damage_uppercut_cont_time: Mapped[float]
    damage_push_cont_time: Mapped[float]
    damage_breath_cont_time: Mapped[float]
    damage_head_shot_cont_time: Mapped[float]
    guard_s_cont_time: Mapped[float]
    guard_l_cont_time: Mapped[float]
    guard_ll_cont_time: Mapped[float]
    guard_brake_cont_time: Mapped[float]
    damage_min_dec_time: Mapped[float]
    damage_s_dec_time: Mapped[float]
    damage_m_dec_time: Mapped[float]
    damage_l_dec_time: Mapped[float]
    damage_blow_s_dec_time: Mapped[float]
    damage_blow_m_dec_time: Mapped[float]
    damage_strike_dec_time: Mapped[float]
    damage_uppercut_dec_time: Mapped[float]
    damage_push_dec_time: Mapped[float]
    damage_breath_dec_time: Mapped[float]
    damage_head_shot_dec_time: Mapped[float]
    guard_s_dec_time: Mapped[float]
    guard_l_dec_time: Mapped[float]
    guard_ll_dec_time: Mapped[float]
    guard_brake_dec_time: Mapped[float]
    
    def __init__(self, id: int, param: KNOCKBACK_PARAM_ST):
        self.id = id
        self.damage_min_cont_time = param.DamageMinContTime
        self.damage_s_cont_time = param.DamageSContTime
        self.damage_m_cont_time = param.DamageMContTime
        self.damage_l_cont_time = param.DamageLContTime
        self.damage_blow_s_cont_time = param.DamageBlowSContTime
        self.damage_blow_m_cont_time = param.DamageBlowMContTime
        self.damage_strike_cont_time = param.DamageStrikeContTime
        self.damage_uppercut_cont_time = param.DamageUppercutContTime
        self.damage_push_cont_time = param.DamagePushContTime
        self.damage_breath_cont_time = param.DamageBreathContTime
        self.damage_head_shot_cont_time = param.DamageHeadShotContTime
        self.guard_s_cont_time = param.GuardSContTime
        self.guard_l_cont_time = param.GuardLContTime
        self.guard_ll_cont_time = param.GuardLLContTime
        self.guard_brake_cont_time = param.GuardBrakeContTime
        self.damage_min_dec_time = param.DamageMinDecTime
        self.damage_s_dec_time = param.DamageSDecTime
        self.damage_m_dec_time = param.DamageMDecTime
        self.damage_l_dec_time = param.DamageLDecTime
        self.damage_blow_s_dec_time = param.DamageBlowSDecTime
        self.damage_blow_m_dec_time = param.DamageBlowMDecTime
        self.damage_strike_dec_time = param.DamageStrikeDecTime
        self.damage_uppercut_dec_time = param.DamageUppercutDecTime
        self.damage_push_dec_time = param.DamagePushDecTime
        self.damage_breath_dec_time = param.DamageBreathDecTime
        self.damage_head_shot_dec_time = param.DamageHeadShotDecTime
        self.guard_s_dec_time = param.GuardSDecTime
        self.guard_l_dec_time = param.GuardLDecTime
        self.guard_ll_dec_time = param.GuardLLDecTime
        self.guard_brake_dec_time = param.GuardBrakeDecTime
