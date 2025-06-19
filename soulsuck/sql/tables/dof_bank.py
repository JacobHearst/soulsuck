from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import DOF_BANK


class DofBank(Base):
    __tablename__ = "dof_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    far_blur_start_distance: Mapped[float]
    far_blur_end_distance: Mapped[float]
    far_blur_magnitude: Mapped[int]
    near_blur_start_distance: Mapped[float]
    near_blur_end_distance: Mapped[float]
    near_blur_magnitude: Mapped[int]
    blur_squared_dispersion: Mapped[float]
    
    def __init__(self, id: int, param: DOF_BANK):
        self.id = id
        self.far_blur_start_distance = param.FarBlurStartDistance
        self.far_blur_end_distance = param.FarBlurEndDistance
        self.far_blur_magnitude = param.FarBlurMagnitude
        self.near_blur_start_distance = param.NearBlurStartDistance
        self.near_blur_end_distance = param.NearBlurEndDistance
        self.near_blur_magnitude = param.NearBlurMagnitude
        self.blur_squared_dispersion = param.BlurSquaredDispersion
