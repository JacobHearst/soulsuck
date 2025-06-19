from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import NPC_THINK_PARAM_ST


class NpcThinkParamST(Base):
    __tablename__ = "npc_think_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    logic_id: Mapped[int]
    battle_id: Mapped[int]
    near_distance: Mapped[float]
    mid_distance: Mapped[float]
    far_distance: Mapped[float]
    out_of_range_distance: Mapped[float]
    retreat_time_after_hitting_enemy_wall: Mapped[float]
    caution_goal_id: Mapped[int]
    stuck_animation_id: Mapped[int]
    search_goal_id: Mapped[int]
    help_call_response_animation: Mapped[int]
    help_call_send_animation: Mapped[int]
    sight_distance: Mapped[int]
    hearing_distance: Mapped[int]
    hearing_cut_distance: Mapped[int]
    smell_distance: Mapped[int]
    max_retreat_distance: Mapped[int]
    battle_retreat_distance: Mapped[int]
    retreat_battle_start_distance: Mapped[int]
    non_battle_act_life: Mapped[int]
    search_time_before_retreat: Mapped[int]
    search_distance_before_retreat: Mapped[int]
    sight_forget_time: Mapped[int]
    hearing_forget_time: Mapped[int]
    battle_start_distance: Mapped[int]
    help_group_id: Mapped[int]
    help_call_group_id: Mapped[int]
    target_sys_damage_rate: Mapped[int]
    team_attack_effectivity: Mapped[int]
    sight_range_height: Mapped[int]
    sight_range_width: Mapped[int]
    hearing_range_height: Mapped[int]
    hearing_range_width: Mapped[int]
    help_call_target_min_distance: Mapped[int]
    help_call_friend_max_distance: Mapped[int]
    help_call_forget_time: Mapped[int]
    help_call_min_wait_time: Mapped[int]
    help_call_max_wait_time: Mapped[int]
    caution_goal_action: Mapped[int]
    search_goal_action: Mapped[int]
    help_call_reply_type: Mapped[int]
    ignore_navmesh: Mapped[int]
    skip_arrival_visible_check: Mapped[bool]
    admirer_attribute: Mapped[bool]
    can_fall_off_edges: Mapped[bool]
    can_navigate_wide_spaces: Mapped[bool]
    can_navigate_ladders: Mapped[bool]
    can_navigate_holes: Mapped[bool]
    can_navigate_doors: Mapped[bool]
    can_navigate_inside_walls: Mapped[bool]
    
    def __init__(self, id: int, param: NPC_THINK_PARAM_ST):
        self.id = id
        self.logic_id = param.LogicID
        self.battle_id = param.BattleID
        self.near_distance = param.NearDistance
        self.mid_distance = param.MidDistance
        self.far_distance = param.FarDistance
        self.out_of_range_distance = param.OutOfRangeDistance
        self.retreat_time_after_hitting_enemy_wall = param.RetreatTimeAfterHittingEnemyWall
        self.caution_goal_id = param.CautionGoalID
        self.stuck_animation_id = param.StuckAnimationID
        self.search_goal_id = param.SearchGoalID
        self.help_call_response_animation = param.HelpCallResponseAnimation
        self.help_call_send_animation = param.HelpCallSendAnimation
        self.sight_distance = param.SightDistance
        self.hearing_distance = param.HearingDistance
        self.hearing_cut_distance = param.HearingCutDistance
        self.smell_distance = param.SmellDistance
        self.max_retreat_distance = param.MaxRetreatDistance
        self.battle_retreat_distance = param.BattleRetreatDistance
        self.retreat_battle_start_distance = param.RetreatBattleStartDistance
        self.non_battle_act_life = param.NonBattleActLife
        self.search_time_before_retreat = param.SearchTimeBeforeRetreat
        self.search_distance_before_retreat = param.SearchDistanceBeforeRetreat
        self.sight_forget_time = param.SightForgetTime
        self.hearing_forget_time = param.HearingForgetTime
        self.battle_start_distance = param.BattleStartDistance
        self.help_group_id = param.HelpGroupID
        self.help_call_group_id = param.HelpCallGroupID
        self.target_sys_damage_rate = param.TargetSysDamageRate
        self.team_attack_effectivity = param.TeamAttackEffectivity
        self.sight_range_height = param.SightRangeHeight
        self.sight_range_width = param.SightRangeWidth
        self.hearing_range_height = param.HearingRangeHeight
        self.hearing_range_width = param.HearingRangeWidth
        self.help_call_target_min_distance = param.HelpCallTargetMinDistance
        self.help_call_friend_max_distance = param.HelpCallFriendMaxDistance
        self.help_call_forget_time = param.HelpCallForgetTime
        self.help_call_min_wait_time = param.HelpCallMinWaitTime
        self.help_call_max_wait_time = param.HelpCallMaxWaitTime
        self.caution_goal_action = param.CautionGoalAction
        self.search_goal_action = param.SearchGoalAction
        self.help_call_reply_type = param.HelpCallReplyType
        self.ignore_navmesh = param.IgnoreNavmesh
        self.skip_arrival_visible_check = bool(param.SkipArrivalVisibleCheck)
        self.admirer_attribute = bool(param.AdmirerAttribute)
        self.can_fall_off_edges = param.CanFallOffEdges
        self.can_navigate_wide_spaces = param.CanNavigateWideSpaces
        self.can_navigate_ladders = param.CanNavigateLadders
        self.can_navigate_holes = param.CanNavigateHoles
        self.can_navigate_doors = param.CanNavigateDoors
        self.can_navigate_inside_walls = param.CanNavigateInsideWalls
