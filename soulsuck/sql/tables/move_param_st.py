from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import MOVE_PARAM_ST


class MoveParamST(Base):
    __tablename__ = "move_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    still_animation: Mapped[int]
    walk_forward_animation: Mapped[int]
    walk_backward_animation: Mapped[int]
    strafe_left_animation: Mapped[int]
    strafe_right_animation: Mapped[int]
    run_forward_animation: Mapped[int]
    run_backward_animation: Mapped[int]
    strafe_run_left_animation: Mapped[int]
    strafe_run_right_animation: Mapped[int]
    sprint_forward_animation: Mapped[int]
    roll_forward_animation: Mapped[int]
    roll_backward_animation: Mapped[int]
    roll_left_animation: Mapped[int]
    roll_right_animation: Mapped[int]
    turn_left_animation: Mapped[int]
    turn_right_animation: Mapped[int]
    large_turn_left_animation: Mapped[int]
    large_turn_right_animation: Mapped[int]
    backstep_animation: Mapped[int]
    hover_animation: Mapped[int]
    fly_forward_animation: Mapped[int]
    fly_forward_left_animation: Mapped[int]
    fly_forward_right_animation: Mapped[int]
    fly_forward_left2_animation: Mapped[int]
    fly_forward_right2_animation: Mapped[int]
    fly_forward_fast_animation: Mapped[int]
    fly_forward_left_fast_animation: Mapped[int]
    fly_forward_right_fast_animation: Mapped[int]
    fly_forward_left_fast2_animation: Mapped[int]
    fly_forward_right_fast2_animation: Mapped[int]
    running_roll_forward_animation: Mapped[int]
    running_roll_backward_animation: Mapped[int]
    running_roll_left_animation: Mapped[int]
    running_roll_right_animation: Mapped[int]
    analog_movement: Mapped[int]
    
    def __init__(self, id: int, move_param: MOVE_PARAM_ST):
        self.id = id
        self.still_animation = move_param.StillAnimation
        self.walk_forward_animation = move_param.WalkForwardAnimatiom
        self.walk_backward_animation = move_param.WalkBackwardAnimation
        self.strafe_left_animation = move_param.StrafeLeftAnimation
        self.strafe_right_animation = move_param.StrafeRightAnimation
        self.run_forward_animation = move_param.RunForwardAnimation
        self.run_backward_animation = move_param.RunBackwardAnimation
        self.strafe_run_left_animation = move_param.StrafeRunLeftAnimation
        self.strafe_run_right_animation = move_param.StrafeRunRightAnimation
        self.sprint_forward_animation = move_param.SprintForwardAnimation
        self.roll_forward_animation = move_param.RollForwardAnimation
        self.roll_backward_animation = move_param.RollBackwardAnimation
        self.roll_left_animation = move_param.RollLeftAnimation
        self.roll_right_animation = move_param.RollRightAnimation
        self.turn_left_animation = move_param.TurnLeftAnimation
        self.turn_right_animation = move_param.TurnRightAnimation
        self.large_turn_left_animation = move_param.LargeTurnLeftAnimation
        self.large_turn_right_animation = move_param.LargeTurnRightAnimation
        self.backstep_animation = move_param.BackstepAnimation
        self.hover_animation = move_param.HoverAnimation
        self.fly_forward_animation = move_param.FlyForwardAnimation
        self.fly_forward_left_animation = move_param.FlyForwardLeftAnimation
        self.fly_forward_right_animation = move_param.FlyForwardRightAnimation
        self.fly_forward_left2_animation = move_param.FlyForwardLeft2Animation
        self.fly_forward_right2_animation = move_param.FlyForwardRight2Animation
        self.fly_forward_fast_animation = move_param.FlyForwardFastAnimation
        self.fly_forward_left_fast_animation = move_param.FlyForwardLeftFastAnimation
        self.fly_forward_right_fast_animation = move_param.FlyForwardRightFastAnimation
        self.fly_forward_left_fast2_animation = move_param.FlyForwardLeftFast2Animation
        self.fly_forward_right_fast2_animation = move_param.FlyForwardRightFast2Animation
        self.running_roll_forward_animation = move_param.RunningRollForwardAnimation
        self.running_roll_backward_animation = move_param.RunningRollBackwardAnimation
        self.running_roll_left_animation = move_param.RunningRollLeftAnimation
        self.running_roll_right_animation = move_param.RunningRollRightAnimation
        self.analog_movement = move_param.AnalogMovement