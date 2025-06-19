from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import MENU_PARAM_COLOR_TABLE_ST


class MenuParamColorTableST(Base):
    __tablename__ = "menu_param_color_table_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    red_channel: Mapped[int]
    green_channel: Mapped[int]
    blue_channel: Mapped[int]
    alpha_channel: Mapped[int]
    
    def __init__(self, id: int, param: MENU_PARAM_COLOR_TABLE_ST):
        self.id = id
        self.red_channel = param.RedChannel
        self.green_channel = param.GreenChannel
        self.blue_channel = param.BlueChannel
        self.alpha_channel = param.AlphaChannel
