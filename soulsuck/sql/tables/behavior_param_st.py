from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import BEHAVIOR_PARAM_ST


class BehaviorParamST(Base):
    __tablename__ = "behavior_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    variation_id: Mapped[int]
    behavior_judge_id: Mapped[int]
    ezstate_behavior_type: Mapped[int]
    reference_type: Mapped[int]
    _pad0: Mapped[bytes]
    reference_id: Mapped[int]
    vfx_variation_id: Mapped[int]
    stamina_cost: Mapped[int]
    durability_cost: Mapped[int]
    category: Mapped[int]
    humanity_cost: Mapped[int]
    _pad1: Mapped[bytes]
    
    def __init__(self, id: int, source: BEHAVIOR_PARAM_ST):
        self.id = id
        self.variation_id = source.VariationID
        self.behavior_judge_id = source.BehaviorJudgeID
        self.ezstate_behavior_type = source.EzstateBehaviorType
        self.reference_type = source.ReferenceType
        self._pad0 = source._Pad0
        self.reference_id = source.ReferenceID
        self.vfx_variation_id = source.VFXVariationID
        self.stamina_cost = source.StaminaCost
        self.durability_cost = source.DurabilityCost
        self.category = source.Category
        self.humanity_cost = source.HumanityCost
        self._pad1 = source._Pad1