from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import QWC_CHANGE_PARAM_ST


class QwcChangeParamST(Base):
    __tablename__ = "qwc_change_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    pc_attr_b: Mapped[int]
    pc_attr_w: Mapped[int]
    pc_attr_l: Mapped[int]
    pc_attr_r: Mapped[int]
    area_attr_b: Mapped[int]
    area_attr_w: Mapped[int]
    area_attr_l: Mapped[int]
    area_attr_r: Mapped[int]
    
    def __init__(self, id: int, param: QWC_CHANGE_PARAM_ST):
        self.id = id
        self.pc_attr_b = param.PcAttrB
        self.pc_attr_w = param.PcAttrW
        self.pc_attr_l = param.PcAttrL
        self.pc_attr_r = param.PcAttrR
        self.area_attr_b = param.AreaAttrB
        self.area_attr_w = param.AreaAttrW
        self.area_attr_l = param.AreaAttrL
        self.area_attr_r = param.AreaAttrR
