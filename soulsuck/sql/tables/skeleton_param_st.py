from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import SKELETON_PARAM_ST


class SkeletonParamSt(Base):
    __tablename__ = "skeleton_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    neck_turn_gain: Mapped[float]
    original_ground_height_ms: Mapped[int]
    min_ankle_height_ms: Mapped[int]
    max_ankle_height_ms: Mapped[int]
    cosine_max_knee_angle: Mapped[int]
    cosine_min_knee_angle: Mapped[int]
    foot_planted_ankle_height_ms: Mapped[int]
    foot_raised_ankle_height_ms: Mapped[int]
    raycast_distance_up: Mapped[int]
    raycast_distance_down: Mapped[int]
    foot_end_lsx: Mapped[int]
    foot_end_lsy: Mapped[int]
    foot_end_lsz: Mapped[int]
    on_off_gain: Mapped[int]
    ground_ascending_gain: Mapped[int]
    ground_descending_gain: Mapped[int]
    foot_raised_gain: Mapped[int]
    foot_planted_gain: Mapped[int]
    foot_unlock_gain: Mapped[int]
    knee_axis_type: Mapped[int]
    use_foot_locking: Mapped[int]
    foot_placement_on: Mapped[int]
    twist_knee_axis_type: Mapped[int]
    neck_turn_priority: Mapped[int]
    neck_turn_max_angle: Mapped[int]
    
    def __init__(self, id: int, skeleton_param: SKELETON_PARAM_ST):
        self.id = id
        self.neck_turn_gain = skeleton_param.NeckTurnGain
        self.original_ground_height_ms = skeleton_param.OriginalGroundHeightMS
        self.min_ankle_height_ms = skeleton_param.MinAnkleHeightMS
        self.max_ankle_height_ms = skeleton_param.MaxAnkleHeightMS
        self.cosine_max_knee_angle = skeleton_param.CosineMaxKneeAngle
        self.cosine_min_knee_angle = skeleton_param.CosineMinKneeAngle
        self.foot_planted_ankle_height_ms = skeleton_param.FootPlantedAnkleHeightMS
        self.foot_raised_ankle_height_ms = skeleton_param.FootRaisedAnkleHeightMS
        self.raycast_distance_up = skeleton_param.RaycastDistanceUp
        self.raycast_distance_down = skeleton_param.RaycastDistanceDown
        self.foot_end_lsx = skeleton_param.FootEndLSX
        self.foot_end_lsy = skeleton_param.FootEndLSY
        self.foot_end_lsz = skeleton_param.FootEndLSZ
        self.on_off_gain = skeleton_param.OnOffGain
        self.ground_ascending_gain = skeleton_param.GroundAscendingGain
        self.ground_descending_gain = skeleton_param.GroundDescendingGain
        self.foot_raised_gain = skeleton_param.FootRaisedGain
        self.foot_planted_gain = skeleton_param.FootPlantedGain
        self.foot_unlock_gain = skeleton_param.FootUnlockGain
        self.knee_axis_type = skeleton_param.KneeAxisType
        self.use_foot_locking = skeleton_param.UseFootLocking
        self.foot_placement_on = skeleton_param.FootPlacementOn
        self.twist_knee_axis_type = skeleton_param.TwistKneeAxisType
        self.neck_turn_priority = skeleton_param.NeckTurnPriority
        self.neck_turn_max_angle = skeleton_param.NeckTurnMaxAngle