from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import LOD_BANK


class LodBank(Base):
    __tablename__ = "lod_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    lv01_border_dist: Mapped[float]
    lv01_play_dist: Mapped[float]
    lv12_border_dist: Mapped[float]
    lv12_play_dist: Mapped[float]
    
    def __init__(self, id: int, param: LOD_BANK):
        self.id = id
        self.lv01_border_dist = param.lv01_BorderDist
        self.lv01_play_dist = param.lv01_PlayDist
        self.lv12_border_dist = param.lv12_BorderDist
        self.lv12_play_dist = param.lv12_PlayDist
