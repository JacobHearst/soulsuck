from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import LIGHT_SCATTERING_BANK


class LightScatteringBank(Base):
    __tablename__ = "light_scattering_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    light_rotation_x: Mapped[int]
    light_rotation_y: Mapped[int]
    distance_multiplier: Mapped[int]
    light_red: Mapped[int]
    light_green: Mapped[int]
    light_blue: Mapped[int]
    light_alpha: Mapped[int]
    scattering_direction: Mapped[float]
    rayleigh_coefficient: Mapped[float]
    mie_coefficient: Mapped[float]
    scattering_coefficient: Mapped[int]
    surface_reflectance_red: Mapped[int]
    surface_reflectance_green: Mapped[int]
    surface_reflectance_blue: Mapped[int]
    surface_reflectance_alpha: Mapped[int]
    
    def __init__(self, id: int, param: LIGHT_SCATTERING_BANK):
        self.id = id
        self.light_rotation_x = param.LightRotationX
        self.light_rotation_y = param.LightRotationY
        self.distance_multiplier = param.DistanceMultiplier
        self.light_red = param.LightRed
        self.light_green = param.LightGreen
        self.light_blue = param.LightBlue
        self.light_alpha = param.LightAlpha
        self.scattering_direction = param.ScatteringDirection
        self.rayleigh_coefficient = param.RayleighCoefficient
        self.mie_coefficient = param.MieCoefficient
        self.scattering_coefficient = param.ScatteringCoefficient
        self.surface_reflectance_red = param.SurfaceReflectanceRed
        self.surface_reflectance_green = param.SurfaceReflectanceGreen
        self.surface_reflectance_blue = param.SurfaceReflectanceBlue
        self.surface_reflectance_alpha = param.SurfaceReflectanceAlpha
