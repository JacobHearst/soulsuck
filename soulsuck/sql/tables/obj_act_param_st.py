from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import OBJ_ACT_PARAM_ST


class ObjActParamST(Base):
    __tablename__ = "obj_act_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    prompt_message: Mapped[int]
    failure_message: Mapped[int]
    flag_for_automatic_success: Mapped[int]
    max_action_distance: Mapped[int]
    player_action_animation: Mapped[int]
    non_player_action_animation: Mapped[int]
    success_condition_id1: Mapped[int]
    success_condition_id2: Mapped[int]
    object_action_model_point: Mapped[int]
    object_action_animation: Mapped[int]
    max_player_angle: Mapped[int]
    success_condition1_type: Mapped[int]
    success_condition2_type: Mapped[int]
    max_object_angle: Mapped[int]
    character_snap_type: Mapped[int]
    event_trigger_delay: Mapped[int]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: OBJ_ACT_PARAM_ST):
        self.id = id
        self.prompt_message = source.PromptMessage
        self.failure_message = source.FailureMessage
        self.flag_for_automatic_success = source.FlagForAutomaticSuccess
        self.max_action_distance = source.MaxActionDistance
        self.player_action_animation = source.PlayerActionAnimation
        self.non_player_action_animation = source.NonPlayerActionAnimation
        self.success_condition_id1 = source.SuccessConditionID1
        self.success_condition_id2 = source.SuccessConditionID2
        self.object_action_model_point = source.ObjectActionModelPoint
        self.object_action_animation = source.ObjectActionAnimation
        self.max_player_angle = source.MaxPlayerAngle
        self.success_condition1_type = source.SuccessCondition1Type
        self.success_condition2_type = source.SuccessCondition2Type
        self.max_object_angle = source.MaxObjectAngle
        self.character_snap_type = source.CharacterSnapType
        self.event_trigger_delay = source.EventTriggerDelay
        self._pad0 = source._Pad0