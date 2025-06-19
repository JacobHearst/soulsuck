from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import LENS_FLARE_EX_BANK


class LensFlareExBank(Base):
    __tablename__ = "lens_flare_ex_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    lens_flare_source_rotation_x: Mapped[int]
    lens_flare_source_rotation_y: Mapped[int]
    lens_flare_source_red: Mapped[int]
    lens_flare_source_green: Mapped[int]
    lens_flare_source_blue: Mapped[int]
    lens_flare_source_alpha: Mapped[int]
    lens_flare_source_distance: Mapped[float]
    
    def __init__(self, id: int, param: LENS_FLARE_EX_BANK):
        self.id = id
        self.lens_flare_source_rotation_x = param.LensFlareSourceRotationX
        self.lens_flare_source_rotation_y = param.LensFlareSourceRotationY
        self.lens_flare_source_red = param.LensFlareSourceRed
        self.lens_flare_source_green = param.LensFlareSourceGreen
        self.lens_flare_source_blue = param.LensFlareSourceBlue
        self.lens_flare_source_alpha = param.LensFlareSourceAlpha
        self.lens_flare_source_distance = param.LensFlareSourceDistance
