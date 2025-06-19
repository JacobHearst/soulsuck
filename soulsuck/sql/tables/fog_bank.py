from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import FOG_BANK


class FogBank(Base):
    __tablename__ = "fog_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    fog_start_distance: Mapped[int]
    fog_end_distance: Mapped[int]
    rotation_z: Mapped[int]
    rotation_w: Mapped[int]
    red: Mapped[int]
    green: Mapped[int]
    blue: Mapped[int]
    alpha: Mapped[int]
    
    def __init__(self, id: int, param: FOG_BANK):
        self.id = id
        self.fog_start_distance = param.FogStartDistance
        self.fog_end_distance = param.FogEndDistance
        self.rotation_z = param.RotationZ
        self.rotation_w = param.RotationW
        self.red = param.Red
        self.green = param.Green
        self.blue = param.Blue
        self.alpha = param.Alpha
