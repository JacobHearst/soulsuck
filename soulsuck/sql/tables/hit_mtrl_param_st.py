from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import HIT_MTRL_PARAM_ST


class HitMtrlParamST(Base):
    __tablename__ = "hit_mtrl_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    sound_radius_multiplier: Mapped[float]
    special_effect_1: Mapped[int]
    special_effect_2: Mapped[int]
    foot_effect_height_type: Mapped[int]
    foot_effect_direction_type: Mapped[int]
    terrain_height_type: Mapped[int]
    
    def __init__(self, id: int, param: HIT_MTRL_PARAM_ST):
        self.id = id
        self.sound_radius_multiplier = param.SoundRadiusMultiplier
        self.special_effect_1 = param.SpecialEffect1
        self.special_effect_2 = param.SpecialEffect2
        self.foot_effect_height_type = param.FootEffectHeightType
        self.foot_effect_direction_type = param.FootEffectDirectionType
        self.terrain_height_type = param.TerrainHeightType
