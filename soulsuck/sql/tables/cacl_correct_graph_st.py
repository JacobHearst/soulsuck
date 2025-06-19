from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import CACL_CORRECT_GRAPH_ST


class CaclCorrectGraphST(Base):
    __tablename__ = "cacl_correct_graph_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    stage_max_intercept_0: Mapped[float]
    stage_max_intercept_1: Mapped[float]
    stage_max_intercept_2: Mapped[float]
    stage_max_intercept_3: Mapped[float]
    stage_max_intercept_4: Mapped[float]
    stage_max_slope_0: Mapped[float]
    stage_max_slope_1: Mapped[float]
    stage_max_slope_2: Mapped[float]
    stage_max_slope_3: Mapped[float]
    stage_max_slope_4: Mapped[float]
    adjustment_max_slope_0: Mapped[float]
    adjustment_max_slope_1: Mapped[float]
    adjustment_max_slope_2: Mapped[float]
    adjustment_max_slope_3: Mapped[float]
    adjustment_max_slope_4: Mapped[float]
    initial_levelling_cost_slope: Mapped[float]
    levelling_cost_early_adjustment: Mapped[float]
    late_levelling_cost_slope: Mapped[float]
    late_levelling_cost_threshold: Mapped[float]
    
    def __init__(self, id: int, param: CACL_CORRECT_GRAPH_ST):
        self.id = id
        self.stage_max_intercept_0 = param.StageMaxIntercept0
        self.stage_max_intercept_1 = param.StageMaxIntercept1
        self.stage_max_intercept_2 = param.StageMaxIntercept2
        self.stage_max_intercept_3 = param.StageMaxIntercept3
        self.stage_max_intercept_4 = param.StageMaxIntercept4
        self.stage_max_slope_0 = param.StageMaxSlope0
        self.stage_max_slope_1 = param.StageMaxSlope1
        self.stage_max_slope_2 = param.StageMaxSlope2
        self.stage_max_slope_3 = param.StageMaxSlope3
        self.stage_max_slope_4 = param.StageMaxSlope4
        self.adjustment_max_slope_0 = param.AdjustmentMaxSlope0
        self.adjustment_max_slope_1 = param.AdjustmentMaxSlope1
        self.adjustment_max_slope_2 = param.AdjustmentMaxSlope2
        self.adjustment_max_slope_3 = param.AdjustmentMaxSlope3
        self.adjustment_max_slope_4 = param.AdjustmentMaxSlope4
        self.initial_levelling_cost_slope = param.InitialLevellingCostSlope
        self.levelling_cost_early_adjustment = param.LevellingCostEarlyAdjustment
        self.late_levelling_cost_slope = param.LateLevellingCostSlope
        self.late_levelling_cost_threshold = param.LateLevellingCostThreshold
