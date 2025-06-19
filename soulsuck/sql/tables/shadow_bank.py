from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import SHADOW_BANK


class ShadowBank(Base):
    __tablename__ = "shadow_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    shadow_source_rotation_x: Mapped[int]
    shadow_source_rotation_y: Mapped[int]
    shadow_density_percentage: Mapped[int]
    shadow_red: Mapped[int]
    shadow_green: Mapped[int]
    shadow_blue: Mapped[int]
    shadow_start_distance: Mapped[float]
    shadow_end_distance: Mapped[float]
    head_on_distance_reduction: Mapped[float]
    fade_start_distance: Mapped[float]
    fade_distance: Mapped[float]
    depth_offset: Mapped[float]
    shadow_map_strength: Mapped[float]
    shadow_volume_depth: Mapped[float]
    
    def __init__(self, id: int, shadow_bank: SHADOW_BANK):
        self.id = id
        self.shadow_source_rotation_x = shadow_bank.ShadowSourceRotationX
        self.shadow_source_rotation_y = shadow_bank.ShadowSourceRotationY
        self.shadow_density_percentage = shadow_bank.ShadowDensityPercentage
        self.shadow_red = shadow_bank.ShadowRed
        self.shadow_green = shadow_bank.ShadowGreen
        self.shadow_blue = shadow_bank.ShadowBlue
        self.shadow_start_distance = shadow_bank.ShadowStartDistance
        self.shadow_end_distance = shadow_bank.ShadowEndDistance
        self.head_on_distance_reduction = shadow_bank.HeadOnDistanceReduction
        self.fade_start_distance = shadow_bank.FadeStartDistance
        self.fade_distance = shadow_bank.FadeDistance
        self.depth_offset = shadow_bank.DepthOffset
        self.shadow_map_strength = shadow_bank.ShadowMapStrength
        self.shadow_volume_depth = shadow_bank.ShadowVolumeDepth