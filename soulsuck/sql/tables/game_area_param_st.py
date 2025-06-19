from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import GAME_AREA_PARAM_ST


class GameAreaParamST(Base):
    __tablename__ = "game_area_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    singleplayer_soul_reward: Mapped[int]
    multiplayer_soul_reward: Mapped[int]
    first_humanity_flag: Mapped[int]
    humanity_drop_point1: Mapped[int]
    humanity_drop_point2: Mapped[int]
    humanity_drop_point3: Mapped[int]
    humanity_drop_point4: Mapped[int]
    humanity_drop_point5: Mapped[int]
    humanity_drop_point6: Mapped[int]
    humanity_drop_point7: Mapped[int]
    humanity_drop_point8: Mapped[int]
    humanity_drop_point9: Mapped[int]
    humanity_drop_point10: Mapped[int]
    
    def __init__(self, id: int, source: GAME_AREA_PARAM_ST):
        self.id = id
        self.singleplayer_soul_reward = source.SingleplayerSoulReward
        self.multiplayer_soul_reward = source.MultiplayerSoulReward
        self.first_humanity_flag = source.FirstHumanityFlag
        self.humanity_drop_point1 = source.HumanityDropPoint1
        self.humanity_drop_point2 = source.HumanityDropPoint2
        self.humanity_drop_point3 = source.HumanityDropPoint3
        self.humanity_drop_point4 = source.HumanityDropPoint4
        self.humanity_drop_point5 = source.HumanityDropPoint5
        self.humanity_drop_point6 = source.HumanityDropPoint6
        self.humanity_drop_point7 = source.HumanityDropPoint7
        self.humanity_drop_point8 = source.HumanityDropPoint8
        self.humanity_drop_point9 = source.HumanityDropPoint9
        self.humanity_drop_point10 = source.HumanityDropPoint10