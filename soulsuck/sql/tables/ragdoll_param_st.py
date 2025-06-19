from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import RAGDOLL_PARAM_ST


class RagdollParamST(Base):
    __tablename__ = "ragdoll_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    hierarchy_gain: Mapped[float]
    velocity_damping: Mapped[float]
    accel_gain: Mapped[float]
    velocity_gain: Mapped[float]
    position_gain: Mapped[float]
    max_liner_velocity: Mapped[float]
    max_angular_velocity: Mapped[float]
    snap_gain: Mapped[float]
    enable: Mapped[bool]
    parts_hit_mask_no: Mapped[int]
    
    def __init__(self, id: int, param: RAGDOLL_PARAM_ST):
        self.id = id
        self.hierarchy_gain = param.HierarchyGain
        self.velocity_damping = param.VelocityDamping
        self.accel_gain = param.AccelGain
        self.velocity_gain = param.VelocityGain
        self.position_gain = param.PositionGain
        self.max_liner_velocity = param.MaxLinerVelocity
        self.max_angular_velocity = param.MaxAngularVelocity
        self.snap_gain = param.SnapGain
        self.enable = bool(param.Enable)
        self.parts_hit_mask_no = param.PartsHitMaskNo
