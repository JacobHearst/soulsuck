from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import POINT_LIGHT_BANK


class PointLightBank(Base):
    __tablename__ = "point_light_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    fade_start_distance: Mapped[float]
    fade_end_distance: Mapped[float]
    point_light_red: Mapped[int]
    point_light_green: Mapped[int]
    point_light_blue: Mapped[int]
    point_light_alpha: Mapped[int]
    
    def __init__(self, id: int, param: POINT_LIGHT_BANK):
        self.id = id
        self.fade_start_distance = param.FadeStartDistance
        self.fade_end_distance = param.FadeEndDistance
        self.point_light_red = param.PointLightRed
        self.point_light_green = param.PointLightGreen
        self.point_light_blue = param.PointLightBlue
        self.point_light_alpha = param.PointLightAlpha
